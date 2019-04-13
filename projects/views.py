from django.shortcuts import render
from projects.models import Project
import json

def project_index(request):
	projects = Project.objects.all()
	context = {
		'projects': projects,
	}
	return render(request, 'project_index.html', context)

def project_detail(request, id):
	project = Project.objects.get(pk=id)

	description_sections = project.description.split('<br>')
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
