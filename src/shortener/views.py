from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from .models import KirrURL
from .forms import SubmitUrlForm
from .validators import validate_url,validate_dot_com
from analytics.models import ClickEvent
# Create your views here.
''' 
	These responses act only when Django sends request for them through the urls
'''
'''
	Function based view
'''
def kirr_redirect(request,shortcode=None , *args, **kwargs):#function based view
	'''This line will be an exception if there does not exist a view coresponding to a particular Url '''
	#so
	##obj=KirrURL.objects.get(shortcode=shortcode)
	'''We acn use the try block and take all entries an dfind the on ewe require  '''
	'''
	try:
		obj=KirrURL.objects.get(shortcode=shortcode)
	except:
		obj=KirrURL.objects.all().first()
	return HttpResponse("Hello {sc}".format(sc=obj.url))
	'''
	#-----------------------------------------------------------------------------
					#or use a query set to filter the results 
	#-----------------------------------------------------------------------------
	# obj_url=None
	# qs=KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count()==1:
	# 	obj=qs.first()
	# 	obj_url=obj.url
	#-----------------------------------------------------------------------------
	#				or use 404 module for simplicity
	#-----------------------------------------------------------------------------
	print shortcode
	obj=get_object_or_404(KirrURL,shortcode=shortcode)
	obj_url=obj.url
	''' 
		Now as we have a redirection to be done we replace 
		the normal http response with http response redirect 
	'''
	#return HttpResponse("hello {sc}".format(sc=obj_url))
	return HttpResponseRedirect(obj_url)
'''
	Class Based view
'''
class KirrRedirectView(View):#class based view
	def get(self,request,shortcode=None, *args, **kwargs):
		obj=get_object_or_404(KirrURL , shortcode=shortcode)
		#print("shortcode is ",shortcode)
		#print 'ABCDE'
		print("This get method has obj.url")
		print ("obj.url is " , obj.url)
		obj.url=validate_url(obj.url)
		# return HttpResponse("Hello again{sc}".format(sc=obj.url))
		return HttpResponseRedirect(obj.url)

	#def post(self,request,shortcode=None,*args,**kwargs):

class URLRedirectView(View):#class based view
	def get(self,request,shortcode=None, *args, **kwargs):
		obj=get_object_or_404(KirrURL , shortcode=shortcode)
		#print("shortcode is ",shortcode)
		#print 'ABCDE'
		print("This get method has obj.url")
		print ("obj.url is " , obj.url)
		obj.url=validate_url(obj.url)
		ClickEvent.objects.create_event(obj)
		# return HttpResponse("Hello again{sc}".format(sc=obj.url))
		print ("ClickEvent.objects.create_event(obj) is ",ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)

	#def post(self,request,shortcode=None,*args,**kwargs):


class HomeView(View):
	def get (self , request ,*args,**kwargs):
		#use a django form 
		the_form = SubmitUrlForm()
		context= {
			"title":"URL Shortener",
			"form":the_form
		}
		return render (request,"shortener/home.html",context)

	def post (self ,request,*args,**kwargs)	:
		#to get the value of the data present we use name of the textfield
		# print (request.POST)
		# print (request.POST["url"])
		# print (request.POST.get("url"))
		form = SubmitUrlForm(request.POST)
		context ={
			"title":"Kirr.co",
			"form":form
		}
		#creating template for viewing 
		template="shortener/home.html"
		if form.is_valid():
			#for printing cleaned datprint (form.cleaned_data)
			#print get url from data
			print "form.cleaned_data.get('url') is ",form.cleaned_data.get('url')
			new_url=form.cleaned_data.get("url")
			#new_url=validate_url("url")
			print ("new_url is ",new_url)
			obj,created=KirrURL.objects.get_or_create(url=new_url)
			context={
				"object":obj,
				"created":created,
			}
			if created:
				template="shortener/success.html"
			else:
				template="shortener/already-exists.html"
#replace the html file with templates
#		return render (request,"shortener/home.html",context)
		return render (request,template ,context)
	"""docstring for HomeView"Viewf __init__(self, arg):
	def get (self , request ,*args,**kwargs):
		return render (request,"home.html",{})
		super(HomeView,View.__init__()
		def get (self , request ,*args,**kwargs):
			return render (request,"home.html",{})
		self.arg = arg"""

		