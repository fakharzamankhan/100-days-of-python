from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for data in question_data:
    new_question = Question(data["text"], data["answer"])
    question_bank.append(new_question)

# for question in question_bank:
#     print(question.text)
#     print(question.answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz! ")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
