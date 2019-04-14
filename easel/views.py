from django.shortcuts import render

def error_404(request):
	return render(request,'404.html', {}, status=404)

def error_500(request):
	response = render(request, '500.html')
	response.status_code = 500
	return response
