from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from .utils import code_generator,createShortcode
from .validators import validate_url,validate_dot_com
from django.core.urlresolvers import reverse

# Create your models here.

SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX",15)

class KirrURLManager(models.Manager):
	def all(self , *args ,**kwargs ):
		qs_main = super(KirrURLManager,self).all(*args, **kwargs)
		qs=qs_main.filter(active=True)
		return qs 

	def refresh_shortcodes(self,items=None):
		print (items)
		qs=KirrURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items,int):
			qs=qs.order_by('-id')[:items]
		new_codes=0
		for q in qs:
			q.shortcode=createShortcode(q)
			print(q.shortcode,' ^^ ',q.id)
			q.save()
			new_codes+=1
		return 'New codes created are:{i} '.format(i=new_codes)



class KirrURL( models.Model ):
	url =models.CharField(max_length=220,validators=[validate_url,validate_dot_com])
	'''
	The field shortcode was added after url and we added a few members in url 
	so either we can have a default for all values or we can leave the previous values empty 
	for default we can use:
		shortcode=models.CharField(max_length=15,defaut='mydefaultvalue')
	for null or empty we can use:
		shortcode=models.CharField(max_length=15,null=true)
	 --------------------------------------------------------------------
	 						or
	 --------------------------------------------------------------------
	 we can use :
		shortcode=models.CharField(max_length=15,null=False,blank=False)
	 --------------------------------------------------------------------
	 						or
	 --------------------------------------------------------------------
	just use the provided menu in the terminal and make a default value	
	 --------------------------------------------------------------------
	 						or
	 --------------------------------------------------------------------
	 delete the migration file and database and start a new migration

	'''
	shortcode =models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
	updated   =models.DateTimeField(auto_now=True)#model was saved at that time
	timestamp =models.DateTimeField(auto_now_add=True)#model was created at that time
	active    =models.BooleanField(default=True)
	objects = KirrURLManager()
	for_Mangers = KirrURLManager()


	#empty_date
	#timestamp saves the time every time we add a model
	def save (self , *args , **kwargs):
		# print("shortcode generation")
		if self.shortcode is None or self.shortcode =='':
			self.shortcode= createShortcode(self)
		super(KirrURL,self).save(*args , **kwargs)

	def __str__(self):
		return str(self.url)

	def get_short_url(self):
		#we can use this method for making the shortcode a http link
		print ("shortcode is",self.shortcode)
		# return "http://www.kirr.com:8000/{shortcode}".format(shortcode=self.shortcode)
		#-----------------------------------------------------------
		#						or
		#-----------------------------------------------------------
		#use reverse module from django.core.urlresolvers
		url_path=reverse("scode",kwargs={'shortcode':self.shortcode})
		return "127.0.0.1:8000"+url_path



	 # def __unicode__(self):
		# return str(self.url)
	
# python manage.py makemigrations
# python manage.py migrations