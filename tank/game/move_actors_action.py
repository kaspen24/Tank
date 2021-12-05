from game import constants
from game.action import Action
from game.point import Point
from game.obstacles import Obstacles

class MoveActorsAction(Action):
    """The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if actor.get_velocity():
                    self._move_actor(actor)
                    self._move_actor(cast["obstacle"][0])
                    self._move_actor(cast["obstacle"][1])
                    self._move_actor(cast["obstacle"][2])
                    self._move_actor(cast["obstacle"][3])
                    self._move_actor(cast["obstacle"][4])
                    self._move_actor(cast["obstacle"][5])
                    self._move_actor(cast["obstacle"][6])
                    self._move_actor(cast["obstacle"][7])
                    self._move_actor(cast["obstacle"][8])
                    self._move_actor(cast["obstacle"][9])
                    self._move_actor(cast["obstacle"][10])
                    self._move_actor(cast["obstacle"][11])
                    self._move_actor(cast["obstacle"][12])
                    self._move_actor(cast["obstacle"][13])
                    self._move_actor(cast["obstacle"][14])
                    self._move_actor(cast["robstacle"][0])
                    self._move_actor(cast["robstacle"][1])
                    self._move_actor(cast["robstacle"][2])
                    self._move_actor(cast["robstacle"][3])
                    self._move_actor(cast["robstacle"][4])
                    self._move_actor(cast["robstacle"][5])
                    self._move_actor(cast["robstacle"][6])
                    self._move_actor(cast["robstacle"][7])
                    self._move_actor(cast["robstacle"][8])
                    self._move_actor(cast["robstacle"][9])
                    self._move_actor(cast["robstacle"][10])
                    self._move_actor(cast["robstacle"][11])
                    self._move_actor(cast["robstacle"][12])
                    self._move_actor(cast["robstacle"][13])
                    self._move_actor(cast["robstacle"][14])
                    

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        x = (x + dx) % constants.MAX_X
        y = (y + dy) % constants.MAX_Y   
        
        position = Point(x, y)
        actor.set_position(position)

