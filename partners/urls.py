from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [
  url('ThankYou/', views.thankYou_partner, name='thankYou_partner_view'),
  url('', views.partner, name='partners_view'),
]