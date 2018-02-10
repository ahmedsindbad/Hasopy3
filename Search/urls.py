from django.conf.urls import include, url

from Search import views

##########################
urlpatternns = ['',
                url(r'^/$', views.SearchPageView.as_view()),
]