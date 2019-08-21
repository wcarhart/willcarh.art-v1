from django.http import Http404
from django.shortcuts import render
from projects.models import Project
import json

def project_index(request):
	projects = Project.objects.order_by('importance')
	print(projects)
	context = {
		'projects': projects,
	}
	return render(request, 'project_index.html', context)

def project_detail(request, title):
	project_title = title.replace('--', '%20').replace('-', ' ').replace('%20', ' ')
	try:
		project = Project.objects.get(title__iexact=title)
	except Project.DoesNotExist:
		raise Http404

	description_sections = project.description.split('<section>')
	links_dictionary = json.loads(project.links.replace("'", '"'))
	github = pypi = ''
	if 'GitHub' in links_dictionary.keys():
		github = links_dictionary['GitHub']
	if 'PyPI' in  links_dictionary.keys():
		pypi = links_dictionary['PyPI']

	context = {
		'project': project,
		'description_sections': description_sections,
		'github': github,
		'pypi': pypi
	}
	return render(request, 'project_detail.html', context)
