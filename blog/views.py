from django.shortcuts import render
from .models import Post

def blog_index(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'blog_index.html', context)

def blog_detail(request, title):
	post_title = title.replace('--', '%20').replace('-', ' ').replace('%20', ' ')
	post = Post.objects.get(title=post_title)
	context = {
		'post': post
	}
	return render(request, 'blog_detail.html', context)
