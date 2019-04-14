from django.shortcuts import render
from .models import Post
from bs4 import BeautifulSoup

def blog_index(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'blog_index.html', context)

def blog_detail(request, title):
	post_title = title.replace('--', '%20').replace('-', ' ').replace('%20', ' ')
	post = Post.objects.get(title=post_title)

	sections = post.content.split('<section>')
	formatted_sections = []
	for section in sections:
		formatted_sections.append(parse_section(section))

	context = {
		'post': post,
		'sections': sections
	}
	return render(request, 'blog_detail.html', context)

def parse_section(section):
	"""
	Parses content for blog post for custom formatting
		:section: (str) the section to parse
	"""
	return
