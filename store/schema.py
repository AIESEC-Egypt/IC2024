import graphene
from graphene import ObjectType, relay, Field
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required

from .models import *


class UserType(DjangoObjectType):
    class Meta:
        model = User

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class OrderType(DjangoObjectType):
    class Meta:
        model = Order

class OrderItemType(DjangoObjectType):
    class Meta:
        model = OrderItem
  

class Query(ObjectType):
    all_order_items = graphene.List(OrderItemType, page=graphene.Int(), per_page=graphene.Int())

    @login_required
    def resolve_all_order_items(self, info, **kwargs):
        page = kwargs.get('page', 1)
        per_page = kwargs.get('per_page', 10)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        return OrderItem.objects.all()[start_index:end_index]    


