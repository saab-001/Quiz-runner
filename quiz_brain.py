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
        answer = input(f"Q.{q_num+1}: {ques} (True/False): ")
        self.question_number += 1
        self.answer_check(answer)

    def answer_check(self, user_ans):
        current_question = self.question_list[self.question_number-1]
        right_answer = current_question.answer

        if user_ans.lower() != "true" and user_ans.lower() != "false":
            self.question_number -= 1
            print("\nInvalid Input\n")
            return

        if user_ans.lower() == right_answer.lower():
            print("You are Right!")
            self.score += 1
        else:
            print("You are Wrong!")
        print(f"The correct answer is {right_answer}")
        print(f"Current Score: {self.score}/{self.question_number}\n")
