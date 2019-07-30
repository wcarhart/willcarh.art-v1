"""
Sends emails from a controlled address
"""
import base64
from django.conf import settings
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

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
	message = f"""
Hi Will,

willcarh.art just got a new message from {from_name}. Here's the message:

------
From: {from_name}
Email: {from_email}
Message: {from_message}
------

Have a good one!
The Herald 🦉

"""
	return message

def build_client_message(from_name):
	"""
	Build "client" email message text given the following:
		:from_name: (str) the sender's name
		:from_email: (str) the sender's email address
		:from_message: (str) the sender's message
	"""
	message = f"""
Hi {from_name}!

Nice to meet you! Thanks so much for checking out my website! I'm excited to read your note, and I'll get back to you as soon as I can.

In the meantime, willcarh.art's friendly email bot, the Herald, is sending you this email to confirm your note's delivery. If you're interested in seeing how the Herald sends emails, please check out its code here:
https://github.com/wcarhart/willcarh.art/blob/master/herald.py

Take care,
Will 🦉

"""
	return message

def create_message(sender, to, subject, message_text):
	"""
	Create a message for an email
		:sender: (str) the email address of the sender
		:to: (str) the email address of the receiver
		:subject: (str) the subject of the email
		:message_text: (str) the content of the email
	"""
	message = MIMEText(message_text)
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

def send_message(from_name, from_email, from_message, target=settings.DEFAULT_TARGET_EMAIL):
	"""
	Handle input from outside programs calling Herald
		:from_name: (str) the sender's name
		:from_email: (str) the sender's email address
		:from_message: (str) the sender's message
		:target: (str) the receiver's email address
	"""

	# authenticate with Gmail API
	service = get_gmail_api_instance()
	if service == None:
		print("herald.py: err: could not authenticate with Gmail API")
		print("herald.py: err: no email sent")
		sys.exit(1)

	# build message content
	if target == settings.DEFAULT_TARGET_EMAIL:
		message_text = build_host_message(from_name, from_email, from_message)
		subject = f"willcarh.art: New email from {from_name}"
	else:
		message_text = build_client_message(from_name)
		subject = "Hello from willcarh.art!"

	# create message structure
	message = create_message(settings.SENDER_EMAIL, target, subject, message_text)

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
