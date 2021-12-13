import sys
from game import constants
from game.point import Point
from game.action import Action
from game.score import Score

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
        obstacles = cast["obstacle"]
        robstacles = cast["robstacle"]
        bullets = cast["bullet"]
        ebullets = cast["ebullet"]
        ebulletsp = cast["ebulletp"]
        border = cast["border"]
        score = Score()
        

        for bullet in cast["bullet"]:    

            for obstacle in cast["obstacle"]:
                if self._physics_service.is_collision(obstacle, bullet):
                        obstacles.remove(obstacle)
                        bullets.remove(bullet)
                        constants.SCORE += 1

            for robstacle in cast["robstacle"]:
                if self._physics_service.is_collision(robstacle, bullet):
                        robstacles.remove(robstacle)
                        bullets.remove(bullet)
                        constants.SCORE += 1

            for ebullet in cast["ebullet"]:
                if self._physics_service.is_collision(ebullet, bullet):
                        ebullets.remove(ebullet)
                        #bullets.remove(bullet)
                        

            for ebulletp in cast["ebulletp"]:
                if self._physics_service.is_collision(ebulletp, bullet):
                        ebulletsp.remove(ebulletp)
                        #bullets.remove(bullet)

        score.set_text(f"Score: {constants.SCORE}")
        score.set_position(Point(1, 0))
        cast["score"] = [score]

        for border in cast["border"]:    

            for bullet in cast["bullet"]:
                if self._physics_service.is_collision(bullet, border):
                        bullets.remove(bullet)

            for ebullet in cast["ebullet"]:
                if self._physics_service.is_collision(ebullet, border):
                        ebullets.remove(ebullet)
            
            for ebulletp in cast["ebulletp"]:
                if self._physics_service.is_collision(ebulletp, border):
                        ebulletsp.remove(ebulletp)


        for obstacles in cast["obstacle"]:
            for robstacles in cast["robstacle"]:
                if self._physics_service.is_collision(obstacles, robstacles):
                    obstacles.set_velocity(Point(constants.VELOCITY_DX, constants.RVELOCITY_DY)) 
                    robstacles.set_velocity(Point(constants.RVELOCITY_DX, constants.VELOCITY_DY))

        for tank in cast["tank"]:
            for obstacles in cast["obstacle"]:
                if self._physics_service.is_collision(obstacles, tank):
                    print(f"\033[1;31m GAME OVER\n")
                    print(f"Your score was {constants.SCORE}")
                    print ("")
                    sys.exit()

            for robstacles in cast["robstacle"]:       
                if self._physics_service.is_collision(robstacles, tank):
                    print(f"\033[1;31m GAME OVER\n")
                    print(f"Your score was {constants.SCORE}")
                    print ("")
                    sys.exit()

            for ebullets in cast["ebullet"]:
                if self._physics_service.is_collision(ebullets, tank):
                    print(f"\033[1;31m GAME OVER\n")
                    print(f"Your score was {constants.SCORE}")
                    print ("")
                    sys.exit()

            for ebulletsp in cast["ebulletp"]:
                if self._physics_service.is_collision(ebulletsp, tank):
                    print(f"\033[1;31m GAME OVER\n")
                    print(f"Your score was {constants.SCORE}")
                    print ("")
                    sys.exit()