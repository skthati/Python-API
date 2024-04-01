class Trivia_logic:
    def __init__(self, questions_list):
        self.question_no = 0
        self.score = 0
        self.current_question = None
        self.questions_list = questions_list
    
    def still_have_question(self):
        if self.question_no < len(self.questions_list):
            return True
    
    def next_question(self):
        self.current_question = self.questions_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"{self.question_no}: {self.current_question.question}?")
        self.check_answer(user_answer)
    
    def convert_answer(self, input_text):
        valid_true_values = ["True", "true", "T", "t"]
        valid_false_values = ["False", "false", "F", "f"]
        if input_text in valid_true_values:
            return "t"
        elif input_text in valid_false_values:
            return "f"

    def check_answer(self, user_answer):
        user_answer = self.convert_answer(user_answer)
        correct_answer = self.convert_answer(self.current_question.answer)
        if user_answer == correct_answer:
            self.score += 1
            print("Correct Answer!")
        else:
            print("Wrong Answer")
        if self.question_no != len(self.questions_list):    
            print(f"Your current score is: {self.score}")

