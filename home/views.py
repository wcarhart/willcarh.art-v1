from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmailForm
from herald import build_host_message, build_client_message, send_email

def home(request):

	form = EmailForm()
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			from_name = form.cleaned_data['name']
			from_email = form.cleaned_data['email']
			from_message = form.cleaned_data['message']

			host_message = build_host_message(from_name, from_email, from_message)
			status, smtpcode, message = send_email(
				(host_message, ""),
				subject=f"willcarh.art: New email from {from_name}"
			)
			print(f"Email to host:{message}")

			client_message = build_client_message(from_name, from_email, from_message)
			status, smtpcode, message = send_email(
				(client_message, ""), 
				subject="Hello from willcarh.art!",
				target=from_email
			)
			print(f"Email to client:{message}")

			messages.add_message(request, messages.SUCCESS, "Message sent!")

			return redirect('/#contact')

	context = {
		"form": EmailForm()
	}

	# clear messages
	system_messages = messages.get_messages(request)
	for message in system_messages:
		pass
	system_messages.used = True

	return render(request, 'index.html', context)

def home_redirect(request):
	response = redirect('/#contact')
	return response
