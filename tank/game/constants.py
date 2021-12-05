import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_TANK = os.path.join(os.getcwd(), "./tank/assets/tank.png")
IMAGE_OBSTACLE = os.path.join(os.getcwd(), "./tank/assets/obstacle.png")

SOUND_START = os.path.join(os.getcwd(), "./tank/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./tank/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tank/assets/over.wav")

TANK_X = MAX_X / 2
TANK_Y = MAX_Y - 125

TANK_DX = 8
TANK_DY = TANK_DX * -1

OBSTACLE_X = MAX_X / 2
OBSTACLE_Y = MAX_Y - 25

OBSTACLE_WIDTH = 24
OBSTACLE_HEIGHT = 24

BRICK_SPACE = 5

TANK_SPEED = 15

TANK_WIDTH = 48
TANK_HEIGHT = 24

VELOCITY_DX = 0.1
VELOCITY_DY = 0.1

RVELOCITY_DX = -0.1
RVELOCITY_DY = -0.1