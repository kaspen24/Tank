from game.actor import Actor
from game import constants

class Background(Actor):
    """
    The Background in the Game.
    """
    def __init__(self):
        super().__init__()

        self.set_width(800)
        self.set_height(600)
        self.set_image(constants.IMAGE_BACKGROUND)