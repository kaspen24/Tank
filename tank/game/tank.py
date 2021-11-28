from game.actor import Actor
from game import constants

class Tank(Actor):
    """
    The Tank in the Game that the game uses.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.TANK_WIDTH / 2)
        self.set_height(constants.TANK_HEIGHT /2)
        self.set_image(constants.IMAGE_TANK)
