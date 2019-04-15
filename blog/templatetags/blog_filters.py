from django import template
from projects.models import Project

register = template.Library()

@register.filter(name='urlify')
def urlify(title):
	return '-'.join(title.replace('-', '--').split())
	