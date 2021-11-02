import pandas as pd

INPUT_FILE_RESULTS = './input/survey_results.csv'

class ResultAdapter:
    def __init__(self):
        self.df = pd.read_csv(INPUT_FILE_RESULTS)

    def filter_by_education(self, education):
        return self.df if not education or education < 0 else self.df[self.df['education'] == education]

    def get_question_average_time(self, id, education):
        # if needed, filter by education
        result_df = self.filter_by_education(education)

        # get time elapse column by question ID
        time_column = id.replace('Q', 'E')
        result_df = result_df[time_column]
        
        # calculate mean
        return result_df.mean()

    def get_response_average_grade(self, id, education):
        # if needed, filter by education
        result_df = self.filter_by_education(education)

        # calculate mean
        return result_df[id].mean()