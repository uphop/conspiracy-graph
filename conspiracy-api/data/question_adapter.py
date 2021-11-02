import pandas as pd

INPUT_FILE_QUESTIONS = './input/survey_questions.csv'

class QuestionAdapter:
    def __init__(self):
        self.df = pd.read_csv(INPUT_FILE_QUESTIONS, index_col=0)

    def get_question(self, id):
        return self.df.loc[id]
    
        

    