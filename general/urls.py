from django.urls import re_path as url

from . import views

urlpatterns = [
  url('store/', views.store, name='store'),
  url('tours/', views.tours, name='tours'),
  url('egypt/', views.egypt, name='egypt'),
  url('', views.index, name='index'),
]