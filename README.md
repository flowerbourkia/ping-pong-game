# Ping Pong 🏓

A two-player Pong game built in Python with the Turtle graphics module — smooth paddle controls, a ball that speeds up and changes angle depending on where it hits the paddle, first to 5 wins.

## How to Run

1. Make sure Python 3 is installed (Turtle ships with Python, nothing else to install).
2. Clone the repository:
   ```bash
   git clone https://github.com/flowerbourkia/ping-pong-game
   cd ping-pong-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Controls

| Player | Up | Down |
|--------|----|------|
| Left   | W  | S    |
| Right  | ↑  | ↓    |

| Key | Action |
|-----|--------|
| Space | Start / play again |
| P | Pause / resume |

## Features

- Paddles move smoothly while the key is held and stay on screen
- The ball speeds up after every hit (up to a maximum)
- Hitting the ball with the edge of the paddle sends it at a sharper angle
- First player to 5 points wins
- Settings (speed, winning score, sizes) are all in `config.py`

## Build a Windows .exe

The project includes a PyInstaller spec file and an icon:

```bash
pip install pyinstaller
pyinstaller Ping_Pong.spec
```

The executable is created in the `dist/` folder.

## Files

- `main.py` – Game loop, controls, scoring, pause and restart
- `ball.py` – Ball movement and bounces
- `paddle.py` – Paddle movement
- `score.py` – Score display and on-screen messages
- `config.py` – Game settings
- `Ping_Pong.spec`, `ping_pong.ico` – Windows executable build

## Built With

- Python
- Turtle graphics module
- PyInstaller
