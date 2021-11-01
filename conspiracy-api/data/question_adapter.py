import pandas as pd
from schema.type.question import Question

INPUT_FILE_QUESTIONS = './input/survey_questions.csv'

class QuestionAdapter:
    def __init__(self):
        self.df = pd.read_csv(INPUT_FILE_QUESTIONS, index_col=0)

    def get_question(self, id):
        result_df = self.df.loc[id]
        return Question(id=id, text=result_df['text'])

    def get_question_count(self):
        return len(self.df.index)