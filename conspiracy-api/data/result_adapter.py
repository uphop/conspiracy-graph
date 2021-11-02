import pandas as pd
from schema.question_enum import Education, Urban, Gender, EngNat, Hand, Religion, Race, Voted, Married

INPUT_FILE_RESULTS = './input/survey_results.csv'


class ResultAdapter:
    def __init__(self):
        self.df = pd.read_csv(INPUT_FILE_RESULTS)

    def filter(self, df, education, urban, gender, eng_nat, age, hand, religion, race, voted, married, family_size, major):
        df = df if not education or education == Education.NOT_DEFINED else df[
            df['education'] == education]
        df = df if not urban or urban == Urban.NOT_DEFINED else df[df['urban'] == urban]
        df = df if not gender or gender == Gender.NOT_DEFINED else df[df['gender'] == gender]
        df = df if not eng_nat or eng_nat == EngNat.NOT_DEFINED else df[df['engnat'] == eng_nat]
        df = df if not age or age < 0 else df[df['age'] == age]
        df = df if not hand or hand == Hand.NOT_DEFINED else df[df['hand'] == hand]
        df = df if not religion or religion == Religion.NOT_DEFINED else df[
            df['religion'] == religion]
        df = df if not race or race == Race.NOT_DEFINED else df[df['race'] == race]
        df = df if not voted or voted == Voted.NOT_DEFINED else df[df['voted'] == voted]
        df = df if not married or married == Married.NOT_DEFINED else df[df['married'] == married]
        df = df if not family_size or family_size < 0 else df[df['familysize'] == family_size]
        df = df if not major or len(major) == 0 else df[df['major'] == major]
        return df

    def get_question_average_time(self, id, education, urban, gender, eng_nat, age, hand, religion, race, voted, married, family_size, major):
        # if needed, filter dataframe
        result_df = self.filter(self.df, education, urban, gender, eng_nat,
                                age, hand, religion, race, voted, married, family_size, major)

        # get time elapse column by question ID
        time_column = id.replace('Q', 'E')
        result_df = result_df[time_column]

        # calculate mean
        return result_df.mean()

    def get_response_average_grade(self, id, education, urban, gender, eng_nat, age, hand, religion, race,  voted, married, family_size, major):
        # if needed, filter dataframe
        result_df = self.filter(self.df, education, urban, gender, eng_nat,
                                age, hand, religion, race, voted, married, family_size, major)

        # calculate mean
        return result_df[id].mean()
