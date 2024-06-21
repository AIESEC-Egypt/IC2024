from django.shortcuts import render
from store.models import *

# Create your views here.
def index(request):
  return render(request, 'pages/index.html')

def egypt(request):
  return render(request, 'pages/whyEgypt.html')

def store(request):
  products = Product.objects.filter(product_type=None)
  return render(request, 'pages/merchandise.html', {'products': products})


def tours(request):
  products = Product.objects.filter(product_type="tour").order_by('priority')
  return render(request, 'pages/tours.html', {'products': products})