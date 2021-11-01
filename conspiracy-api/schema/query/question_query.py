import graphene
from schema.type.question import Question
from data.question_adapter import QuestionAdapter

questionAdapter = QuestionAdapter()
    
class QuestionQuery(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.String())

    def resolve_question(root, info, id):
        return questionAdapter.get_question(id)

