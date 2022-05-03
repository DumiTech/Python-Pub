from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_text = data['question']
    question_answer = data['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
# print(question_bank[0].question_text)

quiz_brain = QuizBrain(question_bank)
    
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
    
print("You completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")

# print(question_bank)