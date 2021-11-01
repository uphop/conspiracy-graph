import graphene

class Question(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    average_time = graphene.Float()
    
