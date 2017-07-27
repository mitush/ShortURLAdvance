"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# here import the views fiunctions which will be used to call the html responses
from django.conf.urls import url
from django.contrib import admin
#from shortener.views import kirr_redirect,KirrRedirectView
from shortener.views import HomeView , KirrRedirectView,URLRedirectView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    #using views as class and mthods
   # url(r'^view-1/$',kirr_redirect),
   # url(r'^view-2/$',KirrRedirectView.as_view()),
    #using slugs
    #here if we remove the / and put {,} we define the min and max length so
    # url(r'^a/(?P<shortcode>[\w-]+)/$',kirr_redirect),
   #"""
    #commented for getting home page
   # url(r'^a/(?P<shortcode>[\w-]+)/$',kirr_redirect),
   
    # url(r'^b/(?P<shortcode>[\w-]+)/$',KirrRedirectView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$',URLRedirectView.as_view(),name='scode'),
]
