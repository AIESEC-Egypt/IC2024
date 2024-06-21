from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  description = models.CharField(max_length=500, blank=True, null=True)
  price = models.CharField(max_length=100, blank=True, null=True)
  image = models.CharField(max_length=100, blank=True, null=True)
  product_type = models.CharField(max_length=100, blank=True, null=True)
  priority = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.name
  

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    # You can add more fields such as total_amount, shipping details, etc.

    def __str__(self):
      return self.user.delegate.first_name + "_" + self.user.delegate.last_name + "'s_Order"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)

    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
      return self.product.name + "_" + self.order.user.delegate.first_name + "_" + self.order.user.delegate.last_name