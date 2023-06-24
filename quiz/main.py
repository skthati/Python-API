from data import question_database
from qa_model import Qa_model
from quiz_logic import Quiz_logic

all_question = []

for each_question in question_database:
    question = each_question['question']
    answer = each_question['correct_answer']
    question_object = Qa_model(question=question, answer=answer)
    all_question.append(question_object)

ql = Quiz_logic(all_question)

while ql.still_have_questions():
    ql.next_question()

print(f"Your final Score is {ql.score}")
