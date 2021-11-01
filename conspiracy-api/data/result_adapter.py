import pandas as pd
from schema.type.question import Question

INPUT_FILE_RESULTS = './input/survey_results.csv'

class ResultAdapter:
    def __init__(self):
        self.df = pd.read_csv(INPUT_FILE_RESULTS)

    def get_question_average_time(self, id):
        time_column = id.replace('Q', 'E')
        return self.df[time_column].mean()