from turtle import Turtle

from config import PADDLE_HALF_HEIGHT, PADDLE_LIMIT, PADDLE_SPEED


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_HALF_HEIGHT * 2 / 20, stretch_len=1)
        self.penup()
        self.start_position = position
        self.goto(position)
        self.moving_up = False
        self.moving_down = False

    # key handlers: the paddle moves for as long as the key is held
    def press_up(self):
        self.moving_up = True

    def release_up(self):
        self.moving_up = False

    def press_down(self):
        self.moving_down = True

    def release_down(self):
        self.moving_down = False

    def update(self):
        y = self.ycor()
        if self.moving_up:
            y += PADDLE_SPEED
        if self.moving_down:
            y -= PADDLE_SPEED
        # keep the paddle on the screen
        y = max(-PADDLE_LIMIT, min(PADDLE_LIMIT, y))
        self.goto(self.xcor(), y)

    def reset(self):
        self.moving_up = self.moving_down = False
        self.goto(self.start_position)
