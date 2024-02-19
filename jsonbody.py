import requests
import json

data = {
  "dato1": "valor1",
  "dato2": "valor2",
  "dato3": "valor3",
  "dato4": "valor4",
  "dato5": "valor5",
  "dato6": "valor6"
}

response = requests.post('http://jenkins_url/job/job_name/build', auth=('username', 'password'), data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(response.status_code)