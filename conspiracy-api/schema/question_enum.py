import graphene

# "How much education have you completed?", 1=Less than high school, 2=High school, 3=University degree, 4=Graduate degree
class Education(graphene.Enum):
    LESS_THAN_HIGH_SCHOOL = 1
    HIGH_SCHOOL = 2
    UNIVERSITY_DEGREE = 3
    GRADUATE_DEGREE = 4
    NOT_DEFINED = -1

# "What type of area did you live when you were a child?", 1=Rural (country side), 2=Suburban, 3=Urban (town, city)
class Urban(graphene.Enum):
    RURAL = 1
    SUBURBAN = 2
    URBAN = 3
    NOT_DEFINED = -1

# "What is your gender?", 1=Male, 2=Female, 3=Other
class Gender(graphene.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    NOT_DEFINED = -1

# "Is English your native language?", 1=Yes, 2=No
class EngNat(graphene.Enum):
    YES = 1
    NO = 2
    NOT_DEFINED = -1

# "What hand do you use to write with?", 1=Right, 2=Left, 3=Both
class Hand(graphene.Enum):
    RIGHT = 1
    LEFT = 2
    BOTH = 3
    NOT_DEFINED = -1

# "What is your religion?", 1=Agnostic, 2=Atheist, 3=Buddhist, 4=Christian (Catholic), 5=Christian (Mormon), 6=Christian (Protestant), 7=Christian (Other), 8=Hindu, 9=Jewish, 10=Muslim, 11=Sikh, 12=Other
class Religion(graphene.Enum):
    AGNOSTIC = 1
    ATHEIST = 2
    BUDDHIST = 3
    CHRISTIAN_CATHOLIC = 4
    CHRISTIAN_MORMON = 5
    CHRISTIAN_PROTESTANT = 6
    CHRISTIAN_OTHER = 7
    HINDU = 8
    JEWISH = 9
    MUSLIM = 10
    SIKH = 11
    OTHER = 12
    NOT_DEFINED = -1

# "What is your sexual orientation?", 1=Heterosexual, 2=Bisexual, 3=Homosexual, 4=Asexual, 5=Other
class Orientation(graphene.Enum):
    HETEROSEXUAL = 1
    BISEXUAL = 2
    HOMOSEXUAL = 3
    ASEXUAL = 4
    OTHER = 5
    NOT_DEFINED = 6

# "What is your race?", 1=Asian, 2=Arab, 3=Black, 4=Indigenous Australian, Native American or White***, 5=Other
class Race(graphene.Enum):
    ASIAN = 1
    ARAB = 2
    BLACK = 3
    AUSTRALIAN_AMERICAN_OR_WHITE = 4
    OTHER = 5
    NOT_DEFINED = -1

# "Have you voted in a national election in the past year?", 1=Yes, 2=No
class Voted(graphene.Enum):
    YES = 1
    NO = 2
    NOT_DEFINED = -1

#  "What is your marital status?", 1=Never married, 2=Currently married, 3=Previously married
class Married(graphene.Enum):
    NEVER_MARRIED = 1
    CURRENTLY_MARRIED = 2
    PREVIOUSLY_MARRIED = 3
    NOT_DEFINED = -1

    


