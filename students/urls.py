from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),
]

