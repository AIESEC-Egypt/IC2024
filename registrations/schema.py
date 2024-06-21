import datetime
import graphene
from graphene_django.types import DjangoObjectType
from graphene import relay, ObjectType
from django.contrib.auth import get_user_model, authenticate, login
from graphql_jwt.shortcuts import get_token as create_jwt_token
from graphql_jwt.decorators import login_required
from .models import *  # Import your Delegate model here
import graphql_jwt
from django.http import request, HttpRequest
from graphql_jwt.shortcuts import get_token
from django.contrib.auth import authenticate



class LeadNode(DjangoObjectType):
    class Meta:
        model = Delegate
        interfaces = (relay.Node,)
        convert_choices_to_enum = False

    food = graphene.List(graphene.String)

    def resolve_food(self, info):
         return self.food.values_list('specification', flat=True)
    
class Login(graphene.Mutation):
    token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, username, password):
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
            token = get_token(user)
            return Login(token=token)
        else:
            raise Exception("Invalid username or password")

class Query(ObjectType):
    all_leads = graphene.List(LeadNode, date_from=graphene.String(), page=graphene.Int(), per_page=graphene.Int())
    
    @login_required
    def resolve_all_leads(self, info, **kwargs):
        date_from = kwargs.get('date_from')
        page = kwargs.get('page', 1)
        per_page = kwargs.get('per_page', 10)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        if date_from is not None:
            return Delegate.objects.filter(created_at__range=(date_from, datetime.datetime.now()))[start_index:end_index]
        else:
            return Delegate.objects.all()[start_index:end_index]

class Mutation(graphene.ObjectType):
    login = Login.Field()