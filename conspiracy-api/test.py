import graphene
from graphene.test import Client
from schema.query.question_query import QuestionQuery

schema = graphene.Schema(query=QuestionQuery)
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