from game.actor import Actor
from game import constants
from game import output_service
from game.tank import Tank
from game.point import Point

class Bullets(Actor):
    """
    The Tank in the Game that the game uses.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.BULLET_WIDTH)
        self.set_height(constants.BULLET_HEIGHT)
        self.set_image(constants.IMAGE_BULLET)