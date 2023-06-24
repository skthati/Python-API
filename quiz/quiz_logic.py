class Quiz_logic:
    def __init__(self, question_lst):
        self.question_no = 0
        self.question_lst = question_lst
        self.score = 0
        self.current_question = None
    
    def still_have_questions(self):
        if self.question_no < len(self.question_lst):
            return True
    
    def next_question(self):
        self.current_question = self.question_lst[self.question_no]
        self.question_no += 1
        user_answer = input(f"Question no ({self.question_no}): {self.current_question.question} (True/False):")
        self.check_answer(user_answer)
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            print("You answered correct!\n")
            self.score += 1
        else:
            print("Wrong Answer!")
        
        print(f"Your present score is {self.score}")


