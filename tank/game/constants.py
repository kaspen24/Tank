import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_TANK = os.path.join(os.getcwd(), "./tank/assets/tank7.png")
IMAGE_OBSTACLE = os.path.join(os.getcwd(), "./tank/assets/tanke.png")
IMAGE_ROBSTACLE = os.path.join(os.getcwd(), "./tank/assets/eTankp.png")
IMAGE_BULLET = os.path.join(os.getcwd(), "./tank/assets/bullet7.png")
IMAGE_EBULLET = os.path.join(os.getcwd(), "./tank/assets/Ebullet.png")
IMAGE_EBULLETP = os.path.join(os.getcwd(), "./tank/assets/ebulletp.png")
IMAGE_BACKGROUND = os.path.join(os.getcwd(), "./tank/assets/background1.png")
IMAGE_BORDER = os.path.join(os.getcwd(), "./tank/assets/border.png")

SOUND_START = os.path.join(os.getcwd(), "./tank/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./tank/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./tank/assets/over.wav")

TANK_X = MAX_X / 2
TANK_Y = MAX_Y - 125

TANK_DX = 8
TANK_DY = TANK_DX * -1

OBSTACLE_X = MAX_X / 2
OBSTACLE_Y = MAX_Y - 25

OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 40

BULLET_WIDTH = 28
BULLET_HEIGHT = 30

TANK_SPEED = 15

TANK_WIDTH = 50
TANK_HEIGHT = 50

VELOCITY_DX = 3
VELOCITY_DY = 3

RVELOCITY_DX = -3
RVELOCITY_DY = -3

BULLET_SPEED = -4

SCORE = 0