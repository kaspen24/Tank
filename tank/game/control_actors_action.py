from game import constants
from game.action import Action
from game.tank import Tank
from game.point import Point
from game.bullets import Bullets

class ControlActorsAction(Action):
    """The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        tank = cast["tank"][0] # there's only one in the cast
        tank.set_velocity(direction.scale(constants.TANK_SPEED))

        if  self._input_service.is_space_pressed():
            cast = {}
            tank = Tank()
            bullets = []
            position = tank.get_position()
            velocity = Point(0, constants.VELOCITY_DX)

            bullet = Bullets()
            bullet.set_position(position)
            bullet.set_velocity(velocity)
            bullets.append(bullet)
            cast["bullet"] = bullets
  
