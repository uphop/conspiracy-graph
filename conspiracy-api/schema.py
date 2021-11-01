import graphene
from data import Data

data = Data()

class Question(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    
class Query(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.String())

    def resolve_question(root, info, id):
        return data.get_question(id)

schema = graphene.Schema(query=Query)