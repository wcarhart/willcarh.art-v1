from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100, default='', null=True, blank=True)
	blurb = models.CharField(max_length=100, default='', null=True, blank=True)
	description = models.TextField(default='', null=True, blank=True)
	technology = models.TextField(default='', null=True, blank=True)
	links = models.TextField(default='', null=True, blank=True)
	cover = models.FilePathField(path='/img', default='', null=True, blank=True)
	demo = models.FilePathField(path='/img', default='', null=True, blank=True)
	color = models.CharField(max_length=10, default='', null=True, blank=True)
	democontent = models.FilePathField(path='/demo', default='', null=True, blank=True)
	importance = models.IntegerField(default=0, blank=True, null=True)
	tags = models.TextField(default='', null=True, blank=True)

	def __str__(self):
		return str(self.title)
