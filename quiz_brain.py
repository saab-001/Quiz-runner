import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        if len(self.question_list) == self.question_number:
            return False

    def next_question(self):
        q_num = self.question_number
        q_list = self.question_list
        ques = html.unescape(q_list[q_num].text)
        return f"Q.{q_num+1}: {ques}"

    def answer_check(self, user_ans):
        current_question = self.question_list[self.question_number-1]
        right_answer = current_question.answer

        if user_ans == right_answer:
            self.score += 1
            return True
        else:
            return False
