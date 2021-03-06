"""Ingeneria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import password_reset_done, password_reset, password_reset_confirm, password_reset_complete

from Ingenieria import views

urlpatterns = [
    url(r'', include('acme.urls', namespace='acme')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/$', views.auth_view),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^log/$', views.log, name='log'),
    url(r'^invalid_login/$', views.invalid_login, name='invalid_login'),
    url(r'^reset-password/$', password_reset, {'template_name': 'acme/password_reset_form.html', 'email_template_name': 'acme/password_reset_email.html'},name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'acme/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'acme/password_reset_confirm.html'} ,name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'acme/password_reset_complete.html'},name='password_reset_complete')
]
