from game.actor import Actor
from game import constants

class Obstacles(Actor):
    """
    Are the Obstacles in the Game that the Tank tries to shoot.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.OBSTACLE_WIDTH)
        self.set_height(constants.OBSTACLE_HEIGHT)
        self.set_image(constants.IMAGE_OBSTACLE)

    