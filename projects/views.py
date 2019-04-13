from django.shortcuts import render
from projects.models import Project

def project_index(request):
	projects = Project.objects.all()
	context = {
		'projects': projects,
	}
	return render(request, 'project_index.html', context)

def project_detail(request, id):
	project = Project.objects.get(pk=id)
	description_sections = project.description.split('<br>')
	context = {
		'project': project,
		'description_sections': description_sections
	}
	return render(request, 'project_detail.html', context)
