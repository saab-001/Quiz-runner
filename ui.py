from tkinter import *
from quiz_brain import QuizBrain

BACKGROUND = "#28282B"


class Interface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.is_right = False

        self.window = Tk()
        self.window.title("Quiz-runner")
        self.window.config(width=800, height=800, padx=30, pady=30, bg=BACKGROUND)

        # Score Display

        self.score_board = Label(text=f"\tScore: {self.quiz.score}", fg="white",
                                 font=("Arial", 12, "bold"), bg=BACKGROUND, highlightthickness=0)
        self.score_board.grid(row=0, column=1)

        # Question Screen

        self.screen = Canvas(width=300, height=280, bg="white", highlightthickness=0)

        self.question_display = self.screen.create_text(150,
                                                        140,
                                                        width=280,
                                                        text=f"question",
                                                        font=("Arial", 15, "italic"))

        self.screen.grid(row=1, column=0, columnspan=2, pady=30)

        # Buttons

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0,
                                  command=self.true_checker)
        self.true_button.grid(row=3, column=0)

        self.false_button = Button(image=false_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0,
                                   command=self.false_checker)
        self.false_button.grid(row=3, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):

        self.screen.config(bg="white")
        current_question = self.quiz.next_question()
        self.screen.itemconfig(self.question_display, text=current_question)
        self.quiz.question_number += 1

    def true_checker(self):

        self.is_right = self.quiz.answer_check("True")

        if self.is_right:
            self.score_board.config(text=f"\tScore: {self.quiz.score}")
            self.screen.config(bg="green")

        else:
            self.screen.config(bg="red")

        if self.quiz.still_has_question():
            self.window.after(500, self.get_question)
        else:
            self.false_button["state"] = "disabled"
            self.true_button["state"] = "disabled"
            self.window.after(1000, self.result_announce)

    def false_checker(self):
        self.is_right = self.quiz.answer_check("False")

        if self.is_right:
            self.score_board.config(text=f"\tScore: {self.quiz.score}")
            self.screen.config(bg="green")
        else:
            self.screen.config(bg="red")

        if self.quiz.still_has_question():
            self.window.after(500, self.get_question)
        else:
            self.false_button["state"] = "disabled"
            self.true_button["state"] = "disabled"
            self.window.after(1000, self.result_announce)

    def result_announce(self):
        self.screen.config(bg="white")
        self.screen.itemconfig(self.question_display, text=f"Quiz Completed\nFinal Score: {self.quiz.score}/10")