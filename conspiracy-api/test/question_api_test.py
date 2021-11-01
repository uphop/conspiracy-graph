import requests
import json

url = 'http://localhost:5000/graphql'
headers = {'content-type' : 'application/json'}
query = '''
    query QuestionQuery($id: String) {
      question(id: $id) {
          id
          text
      }
    }
'''
variables = {'id': 'Q1'}
payload = {
    'query': query,
    'variables': variables
}

r = requests.post(url, json=payload, headers=headers)

print(r.status_code)
print(r.text)

json_data = json.loads(r.text)