from django.contrib import admin
from django.urls import path
from . import views
from .views import booktable

urlpatterns = [
    path("",views.index,name="studentportal"),
    path("about/",views.about,name="aboutpage"),
    path("menu/",views.menu,name="menupage"),
    path("booktable/",views.booktable,name="booktablepage")




]