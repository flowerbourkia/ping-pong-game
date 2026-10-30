from turtle import Turtle

from config import FONT_SCORE, FONT_MESSAGE


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

        # separate turtle for the messages in the middle of the screen
        self.banner = Turtle()
        self.banner.hideturtle()
        self.banner.penup()
        self.banner.color("white")

        self.reset()

    def reset(self):
        self.left_score = 0
        self.right_score = 0
        self.hide_message()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.left_score, align="center", font=FONT_SCORE)
        self.goto(100, 220)
        self.write(self.right_score, align="center", font=FONT_SCORE)

    def left_gain(self):
        self.left_score += 1
        self.update_score()

    def right_gain(self):
        self.right_score += 1
        self.update_score()

    def show_message(self, text):
        self.banner.clear()
        self.banner.goto(0, -40)
        self.banner.write(text, align="center", font=FONT_MESSAGE)

    def hide_message(self):
        self.banner.clear()
