from django.shortcuts import render
from herald import send_message
import sys

def error_404(request, exception):
	return render(request,'404.html', {}, status=404)

def error_500(request):
	trace = sys.exc_info()
	send_message(
		debug=True,
		trace=trace
	)
	response = render(request, '500.html')
	response.status_code = 500
	return response
