from infra.api.endpoints.commands.health import HealthEndpointCommand
from infra.api.endpoints.commands.graphql import GraphQLEndpointCommand

endpoint_commands = [
  HealthEndpointCommand,
  GraphQLEndpointCommand
]

def register_routes(app):
  commands = []

  for CommandType in endpoint_commands:
    command = CommandType()
    command.register(app)
    commands.append(command)

  return commands
