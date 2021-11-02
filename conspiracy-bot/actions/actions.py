# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import requests
import json

class ActionGraphQuery(Action):

    def name(self) -> Text:
        return "action_graph_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # check if question ID and fields are filled
        question_id = tracker.get_slot('question_id')
        if len(question_id) == 0:
            return []
        
        question_fields = tracker.get_slot('question_fields')
        if not question_fields or len(question_fields) == 0:
            # if fields are not provided, set the default ones
            question_fields = ['text']

        # prepare and run query
        query = '''
            query QuestionQuery($id: String) {
                question(id: $id) {
                    ''' + ' ' .join(question_fields) + '''
                }
            }
        '''
        variables = {'id': question_id}
        payload = {
            'query': query,
            'variables': variables
        }

        url = 'http://localhost:5000/graphql'
        headers = {'content-type' : 'application/json'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)

        # get values from result and prepare response
        json_data = json.loads(r.text)
        values = json_data['data']['question']
        question_response_fields = ''
        for item in values:
            question_response_fields += '* ' + item + ' is ' + str(values[item]) + '\n'

        question_response = 'Question details are the following: \n' + question_response_fields
        dispatcher.utter_message(text=question_response)

        return [AllSlotsReset()]
