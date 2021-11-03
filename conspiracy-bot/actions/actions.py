from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import requests
import json

CONSPIRACY_GRAPH_API_URL = 'http://localhost:5000/graphql'

class ActionQuestionQuery(Action):

    def name(self) -> Text:
        return "action_question_query"

    def camelCase(self, st):
        output = ''.join(x for x in st.title() if x.isalnum())
        return output[0].lower() + output[1:]

    def get_query_response_education_filter(self, tracker, response_filters):
        requested_response_filters = tracker.get_slot('requested_response_filters') if tracker.get_slot('requested_response_filters') else []
        print('requested_response_filters: ', requested_response_filters)

        if 'education' in requested_response_filters:
            education_type = tracker.get_slot('education_type')
            education_type = education_type.replace(' ', '_').upper()
            response_filters['education'] = education_type
        return response_filters

    def get_query_response_filters(self, tracker):
         # parse filters
        response_filters = {}
        response_filters = self.get_query_response_education_filter(tracker, response_filters)
        print('response_filters: ', response_filters)

        query_response_filters = json.dumps(response_filters).replace('{', '').replace('}', '').replace('"', '')
        query_response_filters = '(' + query_response_filters + ')' if len(query_response_filters) > 0 else ''
        print('query_response_filters: ', query_response_filters)
        
        return query_response_filters

    def get_query_response(self, tracker):
        # parse response fields
        requested_response_fields = tracker.get_slot('requested_response_fields') if tracker.get_slot('requested_response_fields') else []
        # transform requested response fields to camel case
        requested_response_fields = [self.camelCase(item) for item in requested_response_fields]
        print('requested_response_fields: ', requested_response_fields)

        query_response_filters = self.get_query_response_filters(tracker)
        query_response = ' response ' + query_response_filters + ' {' + ' '.join(requested_response_fields) +'} ' if len(requested_response_fields) > 0 else ''
        return query_response

    def get_query(self, tracker):
        requested_question_fields = tracker.get_slot('requested_question_fields') if tracker.get_slot('requested_question_fields') else []
        print('requested_question_fields: ', requested_question_fields)
        
        query_response = self.get_query_response(tracker)
        query_question = ' question(id: $id) {' + ' '.join(requested_question_fields) + query_response + '}'
        query = 'query QuestionQuery($id: String) {' + query_question + '}'

        return query

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # check if question ID and fields are filled
        question_id = tracker.get_slot('question_id')
        if len(question_id) == 0:
            return []

        # prepare and run query
        
        query = self.get_query(tracker)
        print(query)

        variables = {'id': question_id}
        payload = {
            'query': query,
            'variables': variables
        }

        headers = {'content-type': 'application/json'}
        r = requests.post(CONSPIRACY_GRAPH_API_URL, json=payload, headers=headers)
        print(r.text)

        # get values from result and prepare response
        json_data = json.loads(r.text)
        values = json_data['data']['question']
        question_response_fields = ''
        for item in values:
            question_response_fields += '* ' + item + \
                ' is ' + str(values[item]) + '\n'

        question_response = 'Question details are the following: \n' + question_response_fields
        dispatcher.utter_message(text=question_response)

        return [AllSlotsReset()]
