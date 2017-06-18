from django.db import models

class Details(models.Model):
	title = models.CharField(max_length=250)
	content = models.CharField(max_length=250)
	def __str__(self):
		return self.title
