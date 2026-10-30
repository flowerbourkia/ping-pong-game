import random
from turtle import Turtle

from config import (TOP, BALL_RADIUS, BALL_START_SPEED, BALL_MAX_SPEED,
                    SPEED_UP, PADDLE_HALF_HEIGHT, PADDLE_HALF_WIDTH)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.serve(direction=random.choice([-1, 1]))

    def serve(self, direction):
        """Put the ball in the middle and send it left (-1) or right (1)."""
        self.goto(0, 0)
        self.x_move = BALL_START_SPEED * direction
        self.y_move = BALL_START_SPEED * random.choice([-1, 1]) * random.uniform(0.5, 1)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_on_walls(self):
        # only bounce if the ball is still going towards the wall,
        # otherwise it can get stuck flipping direction every frame
        if (self.ycor() > TOP and self.y_move > 0) or (self.ycor() < -TOP and self.y_move < 0):
            self.y_move *= -1

    def bounce_on(self, paddle):
        """Bounce off `paddle` if touching it. Returns True on a hit."""
        going_towards = (paddle.xcor() > 0 and self.x_move > 0) or (paddle.xcor() < 0 and self.x_move < 0)
        touching_x = abs(self.xcor() - paddle.xcor()) <= PADDLE_HALF_WIDTH + BALL_RADIUS
        offset = self.ycor() - paddle.ycor()
        touching_y = abs(offset) <= PADDLE_HALF_HEIGHT + BALL_RADIUS
        if not (going_towards and touching_x and touching_y):
            return False

        speed = min(abs(self.x_move) * SPEED_UP, BALL_MAX_SPEED)
        self.x_move = -speed if self.x_move > 0 else speed
        # hitting near the edge of the paddle sends the ball at a sharper angle
        self.y_move = speed * offset / (PADDLE_HALF_HEIGHT + BALL_RADIUS)
        return True
