from graphene.test import Client
from schema import schema

client = Client(schema)

query = '''
    query GetQuestion($id: String!) {
      question(id: $id) {
          id
          text
      }
    }
'''
params = {"id": "Q1"}
result = client.execute(query, variables=params)

print(result)