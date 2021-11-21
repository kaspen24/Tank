from game.actor import Actor
from game import constants

class Ball(Actor):
    """
    Are the Bricks in the Game that the Ball tries to hit.
    """
    def __init__(self):
        super().__init__()

        self.set_width(constants.BALL_WIDTH)
        self.set_height(constants.BALL_HEIGHT)
        self.set_image(constants.IMAGE_BALL)

    def _check_bounce(self):  

        if self.ball.get_x < 0 and self.ball.velocity.get_x < 0:
                self.ball.bounce_horizontal()

        if self.ball.get_y < 0 and self.ball.velocity_get_y < 0:
                self.ball.bounce_vertical()

        if self.ball.get_y > constants.MAX_Y and self.ball.velocity.get_y > 0:
                self.ball.bounce_vertical()
