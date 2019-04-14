from django.shortcuts import render
from .models import Blog

def blog_index(request):
	blog_entries = Blog.objects.all()
	context = {
		'blogs': blog_entries
	}
	return render(request, 'blog_index.html', context)

def blog_detail(request, title):
	blog_entry = Blog.objects.get(title=title)
	context = {
		'blog': blog_entry
	}
	return render(request, 'blog_detail.html', context)
