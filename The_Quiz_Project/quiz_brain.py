class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question_text}. Type (True/t or False/f): ")
        if user_answer.lower() == 't':
            user_answer = 'True'
        elif user_answer.lower() == 'f':
            user_answer = 'False'
        print(user_answer)
        self.check_answer(user_answer, current_question.question_answer)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong..")
        print(f"The current score is {self.score}/{self.question_number}")
        print()    
    
