import random
from game import constants
from game.point import Point
from game.action import Action

class HandleCollisionsAction(Action):
    """The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        
        ball = cast["balls"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]

        velocity = ball.get_velocity()

        for ball in cast["balls"]:
            if self._physics_service.is_collision(ball, paddle):
                ball.set_velocity(velocity)

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
                bricks.remove(brick)        
"""