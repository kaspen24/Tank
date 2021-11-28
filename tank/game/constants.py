import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./tank/assets/brick-4.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./tank/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./tank/assets/ball.png")
IMAGE_TANK = os.path.join(os.getcwd(), "./tank/assets/bluesquare.png")

SOUND_START = os.path.join(os.getcwd(), "./tank/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./tank/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tank/assets/over.wav")

TANK_X = MAX_X / 2
TANK_Y = MAX_Y - 125

TANK_DX = 8
TANK_DY = TANK_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

TANK_SPEED = 15

PADDLE_WIDTH = 96
PADDLE_HEIGHT = 24

TANK_WIDTH = 0.3
TANK_HEIGHT = 0.3

VELOCITY_DX = 0.01
VELOCITY_DY = 0.01

RVELOCITY_DX = -0.01
RVELOCITY_DY = -0.01