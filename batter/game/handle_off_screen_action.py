from game import constants 
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):

    def execute(self, cast):
        for ball in cast["balls"]:
            
            if self.ball.center.x < 0 and self.ball.velocity.dx < 0:
                self.ball.bounce_horizontal()

            if self.ball.center.y < 0 and self.ball.velocity.dy < 0:
                self.ball.bounce_vertical()

            if self.ball.center.y > SCREEN_HEIGHT and self.ball.velocity.dy > 0:
                self.ball.bounce_vertical()

            x = ball.get_position().get_x()
            y = ball.get_position().get_y()
            dx = ball.get_velocity().get_x()
            dy = ball.get_velocity().get_y()

            if x == 0:
                dx = constants.VELOCITY_DX * -1

            if y == 0:    
                dy = constants.VELOCITY_DY * -1
        
            velocity = Point(dx, dy)
            ball.set_velocity(velocity)   



            



        



        

