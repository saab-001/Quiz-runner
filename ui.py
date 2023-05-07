from tkinter import *

BACKGROUND = "#28282B"
CANVAS_BACKGROUND = "#C9C9CA"
FONT = ("Arial", 12, "bold")


class Interface:

    def __init__(self):
        self.window = Tk()
        self.window.config(width=800, height=800, padx=40, pady=30, bg=BACKGROUND)
        score_board = Text(width=16, height=3, fg="White", font=FONT, bg=BACKGROUND, borderwidth=0)
        score_board.insert(END, "\tScore:")
        score_board.grid(row=0, column=1, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.screen = Canvas(width=300, height=300, bg=CANVAS_BACKGROUND, highlightthickness=0)

        self.screen.grid(row=1, column=0, columnspan=2)

        self.true_button = Button(image=true_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, bg=BACKGROUND, highlightthickness=0, borderwidth=0)
        self.false_button.grid(row=2, column=1, columnspan=2)

        self.window.mainloop()

