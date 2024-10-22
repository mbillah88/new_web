from django.urls import path

from . import views

urlpatterns = [
    path("", views.master, name="master"),
    path("index/", views.index, name="index"),
]