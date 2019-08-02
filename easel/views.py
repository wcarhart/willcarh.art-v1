from django.shortcuts import render
from herald import send_message
import sys
import traceback

def error_404(request, exception):
	return render(request,'404.html', {}, status=404)

def error_500(request):
	exc_type, exc_value, trace = sys.exc_info()
	error_context = {
		'exception_type': exc_type,
		'exception_value': exc_value,
		'stack_trace': traceback.format_exception(exc_type, exc_value, trace),
		'request': request,
	}
	send_message(
		debug=True,
		error_context=error_context
	)
	response = render(request, '500.html')
	response.status_code = 500
	return response
