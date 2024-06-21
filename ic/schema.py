import graphene
import registrations.schema
import store.schema

class Query(registrations.schema.Query, store.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
  
class Mutation(registrations.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)