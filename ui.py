from tkinter import *

BACKGROUND = "#28282B"
FONT = ("Arial", 12, "bold")


class Interface:

    def __init__(self):

        self.window = Tk()
        self.window.title("Quiz-runner")
        self.window.config(width=800, height=800, padx=30, pady=30, bg=BACKGROUND)

        # Score Display

        score_board = Text(width=16, height=2, fg="White", font=FONT, bg=BACKGROUND, borderwidth=0)
        score_board.insert(END, "\tScore:")
        score_board.grid(row=0, column=1, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # Question Screen

        self.screen = Canvas(width=300, height=280, bg="white", highlightthickness=0)
        self.screen.grid(row=1, column=0, columnspan=2)

        # Padding for buttons

        self.butt_pad = Canvas(height=30, width=0, bg=BACKGROUND, highlightthickness=0)
        self.butt_pad.grid(row=2, columnspan=2)

        # Buttons

        self.true_button = Button(image=true_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=3, column=0)

        self.false_button = Button(image=false_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=3, column=1)

        self.window.mainloop()

