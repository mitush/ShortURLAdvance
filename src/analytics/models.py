from __future__ import unicode_literals
from django.db import models
from shortener.models import KirrURL
# Create your models herwwwwwwhcvshcve.

class ClickEventManager(models.Manager):
	def create_event(self,instance):
		if (isinstance(instance,KirrURL)):
			obj,created=self.get_or_create(kirr_url=instance)
			obj.count+=1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	kirr_url = models.OneToOneField(KirrURL)
	count = models.IntegerField(default=0)
	timestamp =models.DateTimeField(auto_now_add=True)#model was created at that time
	active    =models.BooleanField(default=True)
	objects=ClickEventManager()

	
	def __str__(self):
		return "{i}".format(i=self.count)