from tkinter import *
from quiz_brain import QuizBrain
BACKGROUND = "#28282B"


class Interface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz-runner")
        self.window.config(width=800, height=800, padx=30, pady=30, bg=BACKGROUND)

        # Score Display

        score_board = Text(width=16, height=1, fg="White", font=("Arial", 12, "bold"), bg=BACKGROUND, borderwidth=0)
        score_board.insert(END, "\tScore:")
        score_board.grid(row=0, column=1, columnspan=2)

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

        self.true_button = Button(image=true_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=3, column=0)

        self.false_button = Button(image=false_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=3, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        current_question = self.quiz.next_question()
        self.screen.itemconfig(self.question_display, text=current_question)
