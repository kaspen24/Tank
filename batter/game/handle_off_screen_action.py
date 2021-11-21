from game import constants 
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    """The responsibility of this class of objects is to update the game state when actors collide with edge of screen.
    
    Stereotype:
        Controller
    """
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for ball in cast["balls"]: 
            
            dx = constants.VELOCITY_DX
            dy = constants.VELOCITY_DY
            dxr = constants.RVELOCITY_DX
            dyr = constants.RVELOCITY_DY
            
            if ball.get_position().get_x() == 800 or ball.get_position().get_x() == 0:
                velocity = Point(dx, dyr)
            elif ball.get_position().get_y() == 600 or ball.get_position().get_y() == 0:
                velocity = Point(dxr, dy)
            else:
                velocity = Point(dxr,dyr)
        
            ball.set_velocity(velocity)   



            



        



        

