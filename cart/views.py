from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from store.models import *
# Create your views here.

def cart_summary(request):
  cart = Cart(request)
  cart_products = cart.get_prods()
  quantities = cart.get_quants()
  totals = cart.cart_total()
  return render(request, "pages/cart_summary.html", {"cart_products": cart_products, "quantities": quantities, "totals": totals})

def cart_add(request):
  cart = Cart(request)
  
  if request.POST.get('action') == 'post':
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    print(product_id)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=product_qty)

    cart_quantity = cart.__len__()


    response = JsonResponse({'qty': cart_quantity})
    return response

def cart_delete(request):
  cart = Cart(request)
  if request.POST.get('action') == 'post':
    product_id = int(request.POST.get('product_id'))
    cart.delete(product=product_id)

    response = JsonResponse({'product': product_id})
    return response


def cart_update(request):
  cart = Cart(request)
  if request.POST.get('action') == 'post':
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    cart.update(product=product_id, quantity=product_qty)

    
    response = JsonResponse({'qty': product_qty})
    return response
  
def place_order(request):
    if request.user.is_authenticated:
        user = request.user
        cart = request.session.get('session_key', {})
        order = Order.objects.create(user=user)
        if len(cart.items()):
          for product_id, quantity in cart.items():
              product = get_object_or_404(Product, pk=product_id)
              OrderItem.objects.create(order=order, product=product, quantity=quantity)
        else:
           return render(request, "pages/cart_summary.html", {})
        # Clear the cart after placing the order
        request.session['session_key'] = {}
        
        # Redirect to order confirmation page or any other page
        return render(request, "pages/thankYou_order.html", {})
    else:
        # Handle anonymous user, maybe redirect to login page
        return render(request, "pages/index.html", {})
    

