from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^bears/(?P<table>\d+)$', views.another_method)
]