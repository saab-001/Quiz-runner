import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text_data = i["text"]
    answer_data = i["answer"]
    question_bank += [Question(text_data, answer_data)]

selected_question = random.sample(question_bank, 10)
quiz = QuizBrain(selected_question)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"your Final score: {quiz.score}/{len(quiz.question_list)}")
