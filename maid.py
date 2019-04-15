#!/usr/bin/env python3
"""
Cleans the database
"""
import argparse
from subprocess import call

from django.conf import settings
import django

from easel.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()

from projects.models import Project
from blog.models import Post

def clean():
	"""Erase all records in database for repopulating"""
	for project in Project.objects.all():
		project.delete()
	for post in Post.objects.all():
		post.delete()

def build_parser():
	"""Build command line parser"""
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-u', '--update', action='store_true', required=False, default=False, help="if include, will update database using Scribe after cleaning")
	return parser

def main():
	parser = build_parser()
	args = parser.parse_args()
	
	# clean database
	clean()

	# update, if necessary
	if args.update:
		cmd = 'python3 scribe.py'
		call(cmd, shell=True)

if __name__ == '__main__':
	main()