from game.actor import Actor
from game import constants

class Ball(Actor):
    """
    The Ball in the Game that the game uses to break the bricks.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)
