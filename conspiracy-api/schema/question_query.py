import graphene
from data.question_adapter import QuestionAdapter
from data.result_adapter import ResultAdapter
from schema.question_enum import Education, Urban, Gender, EngNat, Hand, Religion, Race, Voted, Married

question_adapter = QuestionAdapter()
result_adapter = ResultAdapter()

class Response(graphene.ObjectType):
    # filters
    id = graphene.ID()
    education = Education()
    urban = Urban()
    gender = Gender()
    eng_nat = EngNat()
    age = graphene.Int()
    hand = Hand()
    religion = Religion()
    race = Race()
    voted = Voted()
    married = Married()
    family_size = graphene.Int()
    major = graphene.String()

    # derived values
    average_time = graphene.Float()
    average_grade = graphene.Float()

    def resolve_average_time(root, info):
        return result_adapter.get_question_average_time(root.id, root.education, root.urban, root.gender, root.eng_nat, root.age,
                                                        root.hand, root.religion, root.race, root. voted, root.married, root.family_size, root.major)

    def resolve_average_grade(root, info):
        return result_adapter.get_response_average_grade(root.id, root.education, root.urban, root.gender, root.eng_nat, root.age,
                                                         root.hand, root.religion, root.race, root. voted, root.married, root.family_size, root.major)


class Question(graphene.ObjectType):
    id = graphene.ID()
    text = graphene.String()
    response = graphene.Field(Response,
                              id=graphene.String(),
                              education=Education(
                                  required=False, default_value=Education.NOT_DEFINED),
                              urban=Urban(required=False,
                                          default_value=Urban.NOT_DEFINED),
                              gender=Gender(required=False,
                                            default_value=Gender.NOT_DEFINED),
                              eng_nat=EngNat(
                                  required=False, default_value=EngNat.NOT_DEFINED),
                              age=graphene.Int(
                                  required=False, default_value=-1),
                              hand=Hand(required=False,
                                        default_value=Hand.NOT_DEFINED),
                              religion=Religion(
                                  required=False, default_value=Religion.NOT_DEFINED),
                              race=Race(required=False,
                                        default_value=Race.NOT_DEFINED),
                              voted=Voted(required=False,
                                          default_value=Voted.NOT_DEFINED),
                              married=Married(
                                  required=False, default_value=Married.NOT_DEFINED),
                              family_size=graphene.Int(
                                  required=False, default_value=-1),
                              major=graphene.String(
                                  required=False, default_value='')
                              )

    def resolve_text(root, info):
        return question_adapter.get_question_text(root.id)

    def resolve_response(root, info, education, urban, gender, eng_nat, age, hand, religion, race, voted, married, family_size, major):
        return Response(id=root.id, education=education, urban=urban, gender=gender, eng_nat=eng_nat, age=age, hand=hand, religion=religion,
                        race=race, voted=voted, married=married, family_size=family_size, major=major)


class QuestionQuery(graphene.ObjectType):
    question = graphene.Field(Question, id=graphene.String())

    def resolve_question(root, info, id):
        return Question(id=id)
