import graphene
from data.question_adapter import QuestionAdapter
from data.result_adapter import ResultAdapter

question_adapter = QuestionAdapter()
result_adapter = ResultAdapter()

# "How much education have you completed?", 1=Less than high school, 2=High school, 3=University degree, 4=Graduate degree
class Education(graphene.Enum):
    LESS_THAN_HIGH_SCHOOL = 1
    HIGH_SCHOOL = 2
    UNIVERSITY_DEGREE = 3
    GRADUATE_DEGREE = 4
    NOT_DEFINED = -1

    @property
    def description(self):
        if self == Education.LESS_THAN_HIGH_SCHOOL:
            return 'Less than high school'
        elif self == Education.HIGH_SCHOOL:
            return 'High school'
        elif self == Education.UNIVERSITY_DEGREE:
            return 'University degree'
        elif self == Education.GRADUATE_DEGREE:
            return 'Graduate degree'
        else:
            return "Not defined"

class Response(graphene.ObjectType):
    id = graphene.ID()
    education = Education()
    average_time = graphene.Float()
    average_grade = graphene.Float()

    def resolve_average_time(root, info):
        return result_adapter.get_question_average_time(root.id, root.education)

    def resolve_average_grade(root, info):
        return result_adapter.get_response_average_grade(root.id, root.education)

class Question(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    response = graphene.Field(Response, id=graphene.String(), education = Education(required=False, default_value=Education.NOT_DEFINED))
    
    def resolve_text(root, info):
        return question_adapter.get_question(root.id)['text']

    def resolve_response(root, info, education):
        print(education)
        return Response(id=root.id, education=education)
    
class QuestionQuery(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.String())

    def resolve_question(root, info, id):
        return Question(id=id)

