"""Shared game settings."""

# Window
WIDTH = 800
HEIGHT = 600

# Field
TOP = 280            # the ball bounces when it reaches +/- TOP
GOAL_X = 400         # a point is scored when the ball goes beyond +/- GOAL_X

# Paddles
PADDLE_X = 350
PADDLE_HALF_HEIGHT = 50
PADDLE_HALF_WIDTH = 10
PADDLE_LIMIT = 240   # paddles can't go higher/lower than this
PADDLE_SPEED = 8     # pixels per frame while a key is held

# Ball
BALL_RADIUS = 10
BALL_START_SPEED = 4
BALL_MAX_SPEED = 12
SPEED_UP = 1.1       # speed multiplier after each paddle hit

# Game
FRAME_MS = 20        # one frame every 20 ms (about 50 frames per second)
WINNING_SCORE = 5

FONT_SCORE = ("Courier", 40, "normal")
FONT_MESSAGE = ("Courier", 22, "bold")
