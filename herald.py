import argparse
from locksmith import Locksmith
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib, ssl

def build_parser():
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('message', type=str, help="the message to put in the body of the email")
	parser.add_argument('-s', '--subject', type=str, required=False, default="", help="if included, will be the subject line of the email")
	return parser

def red(string):
	return f"\033[91m{string}\033[0m"

def green(string):
	return f"\033[92m{string}\033[0m"

def main():
	# parse args
	parser = build_parser()
	args = parser.parse_args()

	# build credentials and context for smtp
	l = Locksmith('willcarhart_admin')
	port = 465
	password = l.get_secret('EMAIL_PASSWORD')
	email = l.get_secret('EMAIL_NAME')
	context = ssl.create_default_context()

	# open connection
	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		try:
			# authenticate
			server.login(email, password)

			# construct email
			sender_email = email
			receiver_email = email
			message = MIMEMultipart("alternative")
			if args.subject:
				message["Subject"] = args.subject
			else:
				message["Subject"] = "MIME test"
			message["From"] = sender_email
			message["To"] = receiver_email
			plaintext = MIMEText(args.message, "plain")
			message.attach(plaintext)

			# send
			server.sendmail(
				sender_email, receiver_email, message.as_string()
			)

			print(green("  Message sent successfully"))
		except SMTPException:
			print(red("  Message could not be sent"))


if __name__ == '__main__':
	main()
