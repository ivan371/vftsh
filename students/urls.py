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
	url(r'^password/change/$', auth_views.password_change, {'post_change_redirect': reverse_lazy('auth_password_change_done')}, name='auth_password_change'),
	url(r'^password/change/done/$', auth_views.password_change_done, name='auth_password_change_done'),
	url(r'^password/reset/$', auth_views.password_reset, {'post_reset_redirect': reverse_lazy('auth_password_reset_done')}, name='auth_password_reset'),
	url(r'^password/reset/complete/$', auth_views.password_reset_complete, name='auth_password_reset_complete'),
	url(r'^password/reset/done/$', auth_views.password_reset_done, name='auth_password_reset_done'),
	url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
	url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
	url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed')
]

from django import get_version
from distutils.version import LooseVersion
if (LooseVersion(get_version()) >= LooseVersion('1.6')):
	urlpatterns += patterns('', url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')}, name='auth_password_reset_confirm'))
else:
	urlpatterns += patterns('', url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')}, name='auth_password_reset_confirm'))


