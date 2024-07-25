from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

questions_bank = []
for question in question_data:
    questions_text = question["question"]
    questions_answer = question["correct_answer"]
    new_question = Question(questions_text, questions_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print("Your final score is " + str(quiz.score))