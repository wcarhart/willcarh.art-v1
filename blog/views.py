from django.shortcuts import render
from .models import Post
from bs4 import BeautifulSoup
import json

def blog_index(request):
	posts = Post.objects.all()[::-1]
	context = {
		'posts': posts
	}
	return render(request, 'blog_index.html', context)

def blog_detail(request, title):
	post_title = title.replace('--', '%20').replace('-', ' ').replace('%20', ' ')
	post = Post.objects.get(title=post_title)

	sections = post.content.split('<section>')
	cover_credit = json.loads(post.cover_credit)
	# print(cover_credit)

	context = {
		'post': post,
		'sections': sections,
		'cover_credit': cover_credit
	}

	return render(request, 'blog_detail.html', context)
