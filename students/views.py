from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib import auth
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def index(request):
	return render(request, 'students/user.html')
