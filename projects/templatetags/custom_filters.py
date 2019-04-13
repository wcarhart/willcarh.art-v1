from django import template
from projects.models import Project

register = template.Library()

@register.filter(name='multiply')
def multiply(a, b):
	return a*b

@register.filter(name='resolve')
def resolve(_, name):
	project = Project.objects.get(title=name)
	return project.id
	