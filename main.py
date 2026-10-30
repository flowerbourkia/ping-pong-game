from turtle import Screen, Turtle

from config import WIDTH, HEIGHT, PADDLE_X, GOAL_X, FRAME_MS, WINNING_SCORE
from paddle import Paddle
from ball import Ball
from score import Score


def draw_center_line():
    pen = Turtle()
    pen.hideturtle()
    pen.color("gray")
    pen.pensize(3)
    pen.penup()
    pen.goto(0, HEIGHT // 2)
    pen.setheading(270)
    for _ in range(HEIGHT // 40):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(20)


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Ping Pong")
        self.screen.tracer(0)

        draw_center_line()
        self.left_paddle = Paddle((-PADDLE_X, 0))
        self.right_paddle = Paddle((PADDLE_X, 0))
        self.ball = Ball()
        self.score = Score()

        self.bind_keys()
        self.running = False
        self.paused = False
        self.score.show_message("Left: W / S     Right: ↑ / ↓\n\nPress SPACE to start")
        self.screen.update()

    def bind_keys(self):
        controls = [
            (self.left_paddle, ["w", "W"], ["s", "S"]),
            (self.right_paddle, ["Up"], ["Down"]),
        ]
        for paddle, up_keys, down_keys in controls:
            for key in up_keys:
                self.screen.onkeypress(paddle.press_up, key)
                self.screen.onkeyrelease(paddle.release_up, key)
            for key in down_keys:
                self.screen.onkeypress(paddle.press_down, key)
                self.screen.onkeyrelease(paddle.release_down, key)
        self.screen.onkey(self.start, "space")
        self.screen.onkey(self.toggle_pause, "p")
        self.screen.listen()

    def start(self):
        if self.running:
            return
        self.score.reset()
        self.left_paddle.reset()
        self.right_paddle.reset()
        self.ball.serve(direction=1)
        self.running = True
        self.paused = False
        self.tick()

    def tick(self):
        if not self.running:
            return
        if not self.paused:
            self.update()
            self.screen.update()
        if self.running:
            self.screen.ontimer(self.tick, FRAME_MS)

    def update(self):
        self.left_paddle.update()
        self.right_paddle.update()
        self.ball.move()
        self.ball.bounce_on_walls()
        self.ball.bounce_on(self.left_paddle)
        self.ball.bounce_on(self.right_paddle)

        if self.ball.xcor() > GOAL_X:
            self.score.left_gain()
            self.after_point(serve_towards=1)    # serve to the player who lost the point
        elif self.ball.xcor() < -GOAL_X:
            self.score.right_gain()
            self.after_point(serve_towards=-1)

    def after_point(self, serve_towards):
        if self.score.left_score >= WINNING_SCORE:
            self.end_game("LEFT PLAYER WINS!")
        elif self.score.right_score >= WINNING_SCORE:
            self.end_game("RIGHT PLAYER WINS!")
        else:
            self.ball.serve(serve_towards)

    def end_game(self, text):
        self.running = False
        self.ball.goto(0, 0)
        self.score.show_message(f"{text}\n\nPress SPACE to play again")
        self.screen.update()

    def toggle_pause(self):
        if not self.running:
            return
        self.paused = not self.paused
        if self.paused:
            self.score.show_message("PAUSED\nPress P to continue")
        else:
            self.score.hide_message()
        self.screen.update()


if __name__ == "__main__":
    Game()
    Screen().mainloop()
