from typing import Text
# import numpy as np 
import pandas as pd

class Data:
    input_file_questions = 'persistance/survey_questions.csv'
    input_file_results = 'persistance/survey_results.csv'

    def __init__(self):
        self.df = pd.read_csv(self.input_file_questions, index_col=0)
    
    def get_question(self, id):
        from schema import Question
        result_df = self.df.loc[id]
        return Question(id=id, text=result_df['text'])