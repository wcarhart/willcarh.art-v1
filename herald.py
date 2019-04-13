#!/usr/bin/env python3
"""
Sends emails from a controlled address
"""

import argparse
from locksmith import Locksmith
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

def build_parser():
	"""
	Build CLI parser
	"""
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('message', type=str, help="the message to put in the body of the email")
	parser.add_argument('-t', '--target', type=str, required=False, default="", help="if included, the receiver's email")
	parser.add_argument('-s', '--subject', type=str, required=False, default="", help="if included, will be the subject line of the email")
	return parser

def red(string):
	"""
	Convert text to red color
		:string: (str) the string to convert to red
	"""
	return f"\033[91m{string}\033[0m"

def green(string):
	"""
	Convert text to green color
		:string: (str) the string to conver to green
	"""
	return f"\033[92m{string}\033[0m"

def build_host_message(from_name, from_email, from_message):
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

def build_client_message(from_name, from_email, from_message):
	message = f"""
Hi {from_name}!

Nice to meet you! Thanks so much for checking out my website! I'm excited to read your note, and I'll get back to you as soon as I can.

In the meantime, willcarh.art's email bot, the Herald, is sending you this email to confirm your note's delivery. If you're interested in 
seeing how the Herald sends emails, please check out its code here: https://github.com/wcarhart/willcarh.art/blob/master/herald.py

Take care,
Will 🦉

"""
	return message

def send_email(message, subject="", target=None, email=None, password=None):
	"""
	Send an email
		:message: (str, str) the (plaintext, HTML) content of the message
		:subject: (str) the subject of the email
		:target: (str) the target recipient email address
		:email: (str) the email address from which emails will be sent
		:password: (str) the email password for the sender email address

		returns :(code, smtpcode, message): where,
			:code: (int) is the herald code (0 is OK, -1 is error)
			:smtpcode: (int) is the session SMTP exit code
			:message: (str) is a user friendly string to output to the console
	"""

	error_msg = red("  Message could not be sent")
	success_msg = green("  Message sent successfully")

	if not isinstance(message, tuple):
		return (-1, -1, error_msg)

	# build credentials and context for smtp
	l = Locksmith('willcarhart_admin')
	if not target:
		target = l.get_secret('TARGET_EMAIL')
	if not email:
		email = l.get_secret('EMAIL_NAME')
	if not password:
		password = l.get_secret('EMAIL_PASSWORD')

	port = 465
	context = ssl.create_default_context()

	# open connection
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		try:
			# authenticate
			server.login(email, password)

			# construct email from bot
			sender_email = email
			receiver_email = target
			draft = MIMEMultipart("alternative")



			if not subject == "":
				draft["Subject"] = subject
			else:
				draft["Subject"] = f"willcarh.art email notification"
			draft["From"] = sender_email
			draft["To"] = receiver_email

			if not message[0] == "":
				plaintext = MIMEText(message[0], "plain")
				draft.attach(plaintext)
			elif not message[1] == "":
				htmltext = MIMEText(message[1], "html")
				draft.attach(htmltext)
			else:
				return (-1, -1, error_msg)

			# send
			smtpcode = server.sendmail(
				sender_email, receiver_email, draft.as_string()
			)

			return (0, smtpcode, success_msg)
		except smtplib.SMTPException:
			return (-1, -1, error_msg)

def main():
	# parse args
	parser = build_parser()
	args = parser.parse_args()

	target = None if args.target == '' else args.target

	status, smtpcode, message = send_email((args.message, ""), subject=args.subject, target=target)
	print(message)

if __name__ == '__main__':
	main()
