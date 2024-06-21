from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [
  url('ThankYou/', views.thankYou, name='thankyou_view'),
  path('setup/<str:uidb64>/<str:token>/', views.setup_account_view, name='setup_account'),
  url('', views.register, name='register_view'),
]