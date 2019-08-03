"""
Sends emails from a controlled address
"""
import base64
import datetime
from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
import sys
import time

def get_gmail_api_instance():
	"""
	Setup Gmail API instance
	"""
	if not os.path.exists('token.pickle'):
		return None

	with open('token.pickle', 'rb') as token:
		creds = pickle.load(token)
	service = build('gmail', 'v1', credentials=creds)
	return service

def build_host_message(from_name, from_email, from_message):
	"""
	Build "host" email message text given the following:
		:from_name: (str) the sender's name
		:from_email: (str) the sender's email address
		:from_message: (str) the sender's message
	"""
	message_text = f"""
Hi Will,

willcarh.art just got a new message from {from_name}. Here's the message:

------
From: {from_name}
Email: {from_email}
Message: 
{from_message}
------

Have a good one!
The Herald 🦉

"""

	message_html = f"""
<html>
	<head>
		<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
		<style>
			body {{font-family: 'Montserrat', sans-serif;}}
		</style>
	</head>
	<body>
		<p>Hi Will,</p>
		<p>willcarh.art just got a new message from {from_name}. Here's the message:</p>
		<p>------<br><strong>From:</strong> <i>{from_name}</i><br><strong>Email:</strong> <i>{from_email}</i><br><strong>Message:</strong><br>{from_message}<br>------</p>
		<p>Have a good one!<br>The Herald 🦉</p>
	</body>
</html>
"""
	return message_text, message_html

def build_client_message(from_name):
	"""
	Build "client" email message text given the following:
		:from_name: (str) the sender's name
		:from_email: (str) the sender's email address
		:from_message: (str) the sender's message
	"""
	message_text = f"""
Hi {from_name}!

Nice to meet you! Thanks so much for checking out my website! I'm excited to read your note, and I'll get back to you as soon as I can.

In the meantime, willcarh.art's friendly email bot, the Herald, is sending you this email to confirm your note's delivery. If you're interested in seeing how the Herald sends emails, please check out its code here:
https://github.com/wcarhart/willcarh.art/blob/master/herald.py

Take care,
Will 🦉

"""

	message_html = f"""
<html>
	<head>
		<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
		<style>
			body {{font-family: 'Montserrat', sans-serif;}}
		</style>
	</head>
	<body>
		<p>Hi {from_name}!</p>
		<p>Nice to meet you! Thanks so much for checking out my website! I'm excited to read your note, and I'll get back to you as soon as I can.</p>
		<p>In the meantime, willcarh.art's friendly email bot, the Herald, is sending you this email to confirm your note's delivery. If you're interested in seeing how the Herald sends emails, please check out its <a href="https://github.com/wcarhart/willcarh.art/blob/master/herald.py" target="_blank">code here</a>.<br></p>
		<p>Take care,<br>Will 🦉</p>
	</body>
</html>
"""
	return message_text, message_html

def build_error_message(error_context):
	"""
	Build an error message to be sent when 500 server errors occur
		:error_context: (dict) error details to include in the body of the email (stack trace, etc.)
	"""
	exception_type = error_context.get('exception_type', "ERROR: INVALID EXCEPTION TYPE")
	exception_value = error_context.get('exception_value', "ERROR: INVALID EXCEPTION VALUE")
	stack_trace = error_context.get('stack_trace', "ERROR: INVALID STACK TRACE")
	stack_trace = "".join(stack_trace)
	request = error_context.get('request')

	message_text = f"""
Hi Will,

willcarh.art just experienced a 500 server error. Here are the details:

------
Timestamp: {datetime.datetime.now()}
Epoch time: {time.time()}
Attempted URL: willcarh.art{request.path}

HTTP details:
└── scheme: {request.scheme}
└── method: {request.method}
└── path: {request.path}
└── path info: {request.path_info}
└── encoding: {request.encoding}
└── content type: {request.content_type}
└── cookies: 
{format_dict(request.COOKIES)}
└── headers: 
{format_dict(request.headers)}

Exception type: {exception_type.__name__}
Exception value: {exception_value}
Full stack trace:
{str(stack_trace)}
------

Best of luck,
The Herald 🦉

"""
	stack_trace = "".join(stack_trace).replace('\n', '<br>').replace('  ', '&nbsp;&nbsp;')
	message_html = f"""
<html>
	<head>
		<link href="https://fonts.googleapis.com/css?family=Montserrat&display=swap" rel="stylesheet">
		<style>
			body {{font-family: 'Montserrat', sans-serif;}}
		</style>
	</head>
	<body>
		<p>Hi Will,</p>
		<p>willcarh.art just experienced a <strong>500 server error</strong>. Here are the details:</p>
		<p>------<br><strong>Timestamp:</strong> <i>{datetime.datetime.now()}</i><br><strong>Epoch time:</strong> <i>{time.time()}</i><br><strong>Attempted URL:</strong> <i>willcarh.art{request.path}</i></p>
		<p><strong>HTTP details:</strong><br>└── <strong>scheme:</strong> <i>{request.scheme}</i><br>└── <strong>method:</strong> <i>{request.method}</i><br>└── <strong>path:</strong> <i>{request.path}</i><br>└── <strong>path info:</strong> <i>{request.path_info}</i><br>└── <strong>encoding:</strong> <i>{request.encoding}</i><br>└── <strong>content type:</strong> <i>{request.content_type}</i><br>└── <strong>cookies:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;{format_dict(request.COOKIES, True)}<br>└── <strong>headers:</strong><br>&nbsp;&nbsp;&nbsp;&nbsp;{format_dict(request.headers, True)}<p>
		<p><strong>Exception type:</strong> <i>{exception_type.__name__}</i><br><strong>Exception value:</strong> <i>{exception_value}</i><br><strong>Full stack trace:</strong><br>{str(stack_trace)}<br>------</p>
		<p>Best of luck,<br>The Herald 🦉</p>
	</body>
</html>
"""
	
	return message_text, message_html

def format_dict(d, html=False):
	"""
	Format a dictionary *nicely*
		:d: (dict) the dictionary to format
	"""
	ret = []
	for key, value in d.items():
		ret.append(f"\t{key}: {value}")
	if html:
		return "<br>&nbsp;&nbsp;&nbsp;&nbsp;".join(ret)
	return "\n".join(ret)

def create_message(sender, to, subject, message_text, message_html=""):
	"""
	Create a message for an email
		:sender: (str) the email address of the sender
		:to: (str) the email address of the receiver
		:subject: (str) the subject of the email
		:message_text: (str) the content of the email
	"""
	message = MIMEMultipart('alternative')
	message.attach(MIMEText(message_text, 'plain'))
	if not message_html == '':
		message.attach(MIMEText(message_html, 'html'))
	message['to'] = to
	message['from'] = sender
	message['subject'] = subject
	raw = base64.urlsafe_b64encode(message.as_bytes())
	raw = raw.decode()
	body = {'raw': raw}
	return body

def send_email(service, user_id, message):
	"""
	Send an email via Gmail API
		:service: (googleapiclient.discovery.Resource) authorized Gmail API service instance
		:user_id: (str) sender's email address, used for special "me" value (authenticated Gmail account)
		:message: (base64) message to be sent
	"""
	try:
		message = (service.users().messages().send(userId=user_id, body=message).execute())
		return message
	except Exception as e:
		print("herald.py: err: problem sending email")
		print(e)

def send_message(from_name="", from_email="", from_message="", target=settings.DEFAULT_TARGET_EMAIL, debug=False, error_context={}):
	"""
	Handle input from outside programs calling Herald
		:from_name: (str) the sender's name
		:from_email: (str) the sender's email address
		:from_message: (str) the sender's message
		:target: (str) the receiver's email address
		:debug: (bool) whether or not to build an error debug message
		:error_context: (dict) error details to include in the body of the email (stack trace, etc.)
	"""

	# authenticate with Gmail API
	service = get_gmail_api_instance()
	if service == None:
		print("herald.py: err: could not authenticate with Gmail API")
		print("herald.py: err: no email sent")
		sys.exit(1)

	# build message content
	if target == settings.DEFAULT_TARGET_EMAIL:
		if debug:
			message_text, message_html = build_error_message(error_context)
			subject = f"500 Server Error"
		else:
			message_text, message_html = build_host_message(from_name, from_email, from_message)
			subject = f"willcarh.art: New email from {from_name}"
	else:
		message_text, message_html = build_client_message(from_name)
		subject = "Hello from willcarh.art!"

	# create message structure
	message = create_message(
		settings.SENDER_EMAIL, 
		target, subject, 
		message_text, 
		message_html=message_html
	)

	# send email
	result = send_email(service, settings.SENDER_EMAIL, message)

	# log metrics
	if not result == None:
		print("===== Gmail API Message Results =====")
		print("STATUS:  message sent successfully")
		print(f"ID:      {result['id']}")
		print(f"TO:      {target}")
		print(f"NAME:    {from_name}")
		print(f"FROM:    {settings.SENDER_EMAIL}")
		print(f"SUBJECT: {subject}")
		print(f"CONTENT: {message_text}")
		print("=====================================")
