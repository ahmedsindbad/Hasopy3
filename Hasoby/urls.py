"""Hasoby URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from Search import views
from polls import views as views1

urlpatterns = [
    url(r'^$', views.varse, name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^search/$', views.tosearchpage, name='search'),
    url(r'^search/poetry/(?P<poet_id>\d+)/$', views.poetryshow, name='poetry'),
    url(r'^polls/poem/(?P<poem_id1>\d+)/$', views1.PollsById.as_view(), name='pollsbyid'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
