from game.actor import Actor
from game import constants

class Bullets(Actor):
    """
    The User's Tanks Bullets.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.BULLET_WIDTH)
        self.set_height(constants.BULLET_HEIGHT)
        self.set_image(constants.IMAGE_BULLET)