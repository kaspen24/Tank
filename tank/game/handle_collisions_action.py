import random
import sys
from game import constants
from game.point import Point
from game.action import Action
from game import obstacles
from game import robstacles


class HandleCollisionsAction(Action):
    """The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """
        Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        tank = cast["tank"][0] # there's only one
        obstacles = cast["obstacle"][0]
        robstacles = cast["robstacle"][0]

        velocity = tank.get_velocity()

        for obstacles in cast["obstacle"]:
            if self._physics_service.is_collision(obstacles, robstacles):
                obstacles.set_velocity(Point(constants.VELOCITY_DX, constants.RVELOCITY_DY))   

        for robstacles in cast["robstacle"]:
            if self._physics_service.is_collision(robstacles, obstacles):
                robstacles.set_velocity(Point(constants.RVELOCITY_DX, constants.VELOCITY_DY))   

        for obstacles in cast["obstacle"]:
            if self._physics_service.is_collision(obstacles, tank):
                print(f"\033[1;31m GAME OVER\n")
                sys.exit()

        for robstacles in cast["robstacle"]:       
            if self._physics_service.is_collision(robstacles, tank):
                print(f"\033[1;31m GAME OVER\n")
                sys.exit() 
