import graphene
from schema.question_types import Question
from data.question_adapter import QuestionAdapter
from data.result_adapter import ResultAdapter

question_adapter = QuestionAdapter()
result_adapter = ResultAdapter()
    
class QuestionQuery(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.String())
    total_count = graphene.Int()

    def resolve_question(root, info, id):
        result = question_adapter.get_question(id)
        result.average_time = result_adapter.get_question_average_time(id)
        return result
    
    def resolve_total_count(root, info):
        return question_adapter.get_question_count()

