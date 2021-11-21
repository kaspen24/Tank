from game.actor import Actor
from game import constants

class Brick(Actor):
    """
    Are the Bricks in the Game that the Ball tries to hit.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)
        self.set_image(constants.IMAGE_BRICK)

    