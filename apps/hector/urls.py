from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^compare$', views.compare),
    url(r'^reset$', views.reset),
    url(r'^', views.odell)
]
