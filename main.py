import random
from ui import Interface
from question_model import Question
from quiz_brain import QuizBrain


def ques_generator():

    from data import question_data

    data = question_data
    question_bank = []
    for i in data:
        text_data = i["question"]
        answer_data = i["correct_answer"]
        question_bank += [Question(text_data, answer_data)]

    return random.sample(question_bank, 10)


selected_questions = ques_generator()

quiz = QuizBrain(selected_questions)
ui = Interface(quiz)
