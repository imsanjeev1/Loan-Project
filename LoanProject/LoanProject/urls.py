"""LoanProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from loanapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^register/$', views.register),
    url(r'^eligibility/$', views.checklimit),
    url(r'^reguser/$', views.reguser),
    url(r'^login/$', views.signin),
    url(r'^signin/$', views.loginpage),
    url(r'^lapply/$', views.loanapply),
    url(r'^history/$', views.history),
    url(r'^apply_loan/$', views.apply_loan),
    url(r'^newuser/$', views.newuser),
]
