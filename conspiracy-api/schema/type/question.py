import graphene

class Question(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
