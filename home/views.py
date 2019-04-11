from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import EmailForm

def home(request):
	print('here')
	return render(request, 'index.html', {})

def get_email(request):
	print('here2')
	if request.method == 'POST':
		print('here')
