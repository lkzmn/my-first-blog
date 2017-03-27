# from __future__ import unicode_literals
# Might need the above, comes as default in Python 2.7 but possibly not in 3.x
# This is what you would see on the webpage (e.g. Author: and blank menu)

from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def _str_(self):
		return self.title

