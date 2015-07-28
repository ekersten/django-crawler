from django.conf.urls import patterns, url
from crawler import views

urlpatterns = patterns ('',
	url(r'^$', views.home, name='home'),
)