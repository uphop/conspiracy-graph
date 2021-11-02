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
import requests
import json

class ActionGraphQuery(Action):

    def name(self) -> Text:
        return "action_graph_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        question_id = tracker.get_slot('question_id')
        print('question_id: ' + question_id)

        question_fields = tracker.get_slot('question_fields')
        print('question_fields: ')
        print(question_fields)

        # extract question from the latest message's text
        full_message_text = tracker.latest_message.get('text')
        print('full_message_text: ' + full_message_text)

        url = 'http://localhost:5000/graphql'
        headers = {'content-type' : 'application/json'}
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

        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        json_data = json.loads(r.text)

        # question_text = json_data['data']['question']['text']
        question_text = 'hello world!'
        dispatcher.utter_message(text=question_text)

        return []
