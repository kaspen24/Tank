from game.actor import Actor
from game import constants
import random

class Robstacles(Actor):
    """
    Are the Obstacles in the Game that the Tank tries to shoot.
    """
    def __init__(self):
        super().__init__()

        self.set_width(random.uniform(0, constants.OBSTACLE_WIDTH))
        self.set_height(random.uniform(0, constants.OBSTACLE_HEIGHT))
        self.set_image(constants.IMAGE_OBSTACLE)

    