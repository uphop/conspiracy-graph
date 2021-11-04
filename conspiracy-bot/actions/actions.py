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

    def string_to_camel(self, st):
        output = ''.join(x for x in st.title() if x.isalnum())
        return output[0].lower() + output[1:]

    def get_query(self, tracker):
        # extract question root fields
        requested_question_fields = tracker.get_slot('requested_question_fields') if tracker.get_slot('requested_question_fields') else []

        # extract response fields
        requested_response_fields = tracker.get_slot('requested_response_fields') if tracker.get_slot('requested_response_fields') else []
        requested_response_fields = [self.string_to_camel(item) for item in requested_response_fields]

        # apply response filters if any provided
        requested_response_filters = tracker.get_slot('requested_response_filters') if tracker.get_slot('requested_response_filters') else []
        response_filters = {}
        response_filters['education'] = tracker.get_slot('education_type').replace(' ', '_').upper() if 'education' in requested_response_filters else 'NOT_DEFINED'
        response_filters['urban'] = tracker.get_slot('area_type').replace(' ', '_').upper() if 'area' in requested_response_filters else 'NOT_DEFINED'
        query_response_filters = json.dumps(response_filters).replace('{', '').replace('}', '').replace('"', '')

        print('requested_question_fields: ', requested_question_fields)
        print('requested_response_fields: ', requested_response_fields)
        print('requested_response_filters: ', requested_response_filters)

        # constract graph query
        query = 'query QuestionQuery($id: String) {'
        query += ' question(id: $id) {'
        query += ' '.join(requested_question_fields)
        if len(requested_response_fields) > 0:
            query += '  response '
            if len(query_response_filters) > 0:
                query += '('
                query += query_response_filters
                query += ')'
            query += ' {'
            query += '    '.join(requested_response_fields)
            query += ' }'
        query += '  }'
        query += '}'

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
