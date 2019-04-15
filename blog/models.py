from django.db import models
import datetime

class Post(models.Model):
	index = models.IntegerField(default=0, blank=True, null=True)
	title = models.CharField(max_length=100, default='', null=True, blank=True)
	subtitle = models.CharField(max_length=100, default='', null=True, blank=True)
	blurb = models.CharField(max_length=250, default='', null=True, blank=True)
	cover = models.FilePathField(path='/img', default='', null=True, blank=True)
	content = models.TextField(default='', null=True, blank=True)
	published = models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)
	author = models.CharField(max_length=100, default='', null=True, blank=True)
	cover_credit = models.TextField(default='', null=True, blank=True)

	def __str__(self):
		return str(self.title)
