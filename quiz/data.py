import requests

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)

question_database = response.json()
question_database = question_database['results']
