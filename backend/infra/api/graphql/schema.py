import graphene

class SystemQueries(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="stranger"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

root_schema = graphene.Schema(query=SystemQueries)
