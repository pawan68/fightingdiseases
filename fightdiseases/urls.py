from django.conf.urls import url, include
from django.contrib import admin
from fightdiseases import views
urlpatterns = [
    url(r'^$', views.index),
]