#!/usr/bin/env python3
"""
Writes new entries to the database
"""
import argparse
import json
import sys

from django.conf import settings
import django

from easel.settings import DATABASES, INSTALLED_APPS
settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
django.setup()

import projects.models

def is_valid_against_schema(entity):
	"""
	Validate if given JSON entity is a valid model in Django ORM
		Valid JSON should have the following fields for each object
		in the list:
		 - class, where value is the name of the Model
		 - contents, where value is the contents for an instance of
		   said class
	"""
	# validate class
	if not 'class' in entity.keys():
		return False
	if not isinstance(entity['class'], str):
		return False
	try:
		Class = getattr(projects.models, entity['class'])
	except AttributeError:
		return False

	# validate contents
	if not 'content' in entity.keys():
		return False
	if not isinstance(entity['content'], dict):
		return False
	class_vars = get_class_vars(Class)
	if not set(class_vars) == set(entity['content'].keys()):
		return False

	return True

def get_class_vars(Class):
	"""Get all custom defined fields from a class"""
	class_vars = [var for var in dir(Class) if not var.startswith('__') and not var.startswith('_') and not callable(getattr(Class, var))]
	meta_vars = ['id', 'pk', 'objects']
	meta_filter = lambda item: not item in meta_vars
	return list(filter(meta_filter, class_vars))

def is_valid_against_table(entity, Class):
	"""Validate if given record from JSON is alredy in database"""
	all_records = Class.objects.all()
	class_vars = get_class_vars(Class)
	entity_fields = entity['content']
	for record in all_records:
		record_fields = {field: getattr(record, field) for field in class_vars}
		if record_fields == entity_fields:
			return False
	return True

def parse_data(entity, index):
	"""Parse data, add to database"""
	Class = getattr(projects.models, entity['class'])
	if not is_valid_against_table(entity, Class):
		print(f"Entity {entity['class']} at index {index} is already in the database")
	else:
		instance = Class(**entity['content'])
		instance.save()
	
def build_parser():
	"""Build command line parser"""
	parser = argparse.ArgumentParser(description=__doc__, formatter_class = argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-f', '--file', type=str, required=False, default='content.json', help='JSON file from which to read content for database')
	return parser

def main():
	parser = build_parser()
	args = parser.parse_args()

	with open(args.file) as json_file:
		json_data = json.load(json_file)
		for index, entity in enumerate(json_data):
			if is_valid_against_schema(entity):
				parse_data(entity, index)
			else:
				print(f"Invalid JSON data found at index {index}")
				continue

if __name__ == '__main__':
	main()
	