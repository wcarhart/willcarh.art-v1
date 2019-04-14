from django import template
from projects.models import Project

register = template.Library()

@register.filter(name='urlify')
def urlify(title, article_number):
	return '-'.join(title.replace('-', '--').split())
	