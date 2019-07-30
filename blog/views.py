from django.http import Http404
from django.shortcuts import render
from .models import Post
import json

def blog_index(request):
	posts = Post.objects.all()[::-1]
	context = {
		'posts': posts
	}
	return render(request, 'blog_index.html', context)

def blog_detail(request, title):
	post_title = title.replace('--', '%20').replace('-', ' ').replace('%20', ' ')
	try:
		post = Post.objects.get(title=post_title)
	except Post.DoesNotExist:
		raise Http404

	cover_credit = json.loads(post.cover_credit)

	context = {
		'post': post,
		'cover_credit': cover_credit
	}

	return render(request, 'blog_detail.html', context)
