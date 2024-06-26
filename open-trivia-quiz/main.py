# from flask import Flask, render_template
from trivia_data import all_questions
from question_answer_object import Question_answer_list
from trivia_logic import Trivia_logic
import requests


questions_list = []

def get_questions():
    for each_question_answer in all_questions:
        question = each_question_answer['question']
        answer = each_question_answer['correct_answer']
        qa_object_list = Question_answer_list(question, answer)
        questions_list.append(qa_object_list)


get_questions()

for each_question in questions_list:
    print(f"{each_question.question} \n Answer: {each_question.answer}")

tl = Trivia_logic(questions_list)

while tl.still_have_question():
    tl.next_question()

print(f"Your final score is: {tl.score}")

# app = Flask(__name__)


# @app.route("/")
# def index():
#     # get_questions()
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run("0.0.0.0", port=8001, debug=True)


