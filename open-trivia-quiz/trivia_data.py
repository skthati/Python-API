import requests

url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean"

response = requests.get(url)
all_data = response.json()

all_questions = all_data['results']
