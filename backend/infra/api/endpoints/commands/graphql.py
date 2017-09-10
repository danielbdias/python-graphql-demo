from bottle import request

from infra.api.endpoints.response import json_response
from infra.api.graphql.schema import root_schema

from collections import namedtuple

def handle_graphql_response(func):
  try:
    result = func()
    output = { 'data': result.data }

    if result.errors is not None:
      output['errors'] = result.errors

    return json_response(output)
  except Error as e:
    print('An error happened executing a GraphQL query. Error: {error}'.format(error=e))
    return json_response({ 'data': None, 'errors': [ e ] })

def execute_post():
  graphql_data = request.json
  graphql_query = graphql_data['query']

  return root_schema.execute(graphql_query)

def execute_introspection():
  DataItem = namedtuple('DataItem', ['data', 'errors'])
  return DataItem(data=root_schema.introspect(), errors=None)

class GraphQLEndpointCommand(object):
  def register(self, app):
    app.route('/graphql', 'OPTIONS', self.execute_introspection_query)
    app.route('/graphql', 'POST', self.execute_post_query)

  def execute_post_query(self):
    return handle_graphql_response(execute_post)

  def execute_introspection_query(self):
    return handle_graphql_response(execute_introspection)
