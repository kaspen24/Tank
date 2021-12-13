from game import constants
from game.action import Action
from game.point import Point
from game.bullets import Bullets
from game.ebullets import Ebullets
from game.ebulletsp import Ebulletsp
import random
from game.obstacles import Obstacles
from game.robstacles import Robstacles


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
        obstacles = cast["obstacle"]

        if  self._input_service.is_space_released():
            bullets = cast["bullet"]
            position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
            velocity = Point(0, constants.BULLET_SPEED)

            bullet = Bullets()
            bullet.set_position(position)
            bullet.set_velocity(velocity)
            bullets.append(bullet)

        if self._input_service.is_b_released():
                velocity = Point(0, constants.BULLET_SPEED * -1)
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)


        if self._input_service.is_down_released():
            obstacles = cast["obstacle"]
            x = random.randint(0, 150)
            y = random.randint(0, 75)
            position = Point(x, y)

            dx = random.uniform(0, constants.VELOCITY_DX)
            dy = random.uniform(0, constants.VELOCITY_DY)
            velocity = Point(dx, dy)

            obstacle = Obstacles()
            obstacle.set_position(position)
            obstacle.set_velocity(velocity)
            obstacles.append(obstacle)

        if self._input_service.is_up_released():
                robstacles = cast["robstacle"]
                x = random.randint(650, 800)
                y = random.randint(525, 600)
                position = Point(x, y)

                dx = random.uniform(0, constants.RVELOCITY_DX)
                dy = random.uniform(0, constants.RVELOCITY_DY)
                velocity = Point(dx, dy)

                robstacle = Robstacles()
                robstacle.set_position(position)
                robstacle.set_velocity(velocity)
                robstacles.append(robstacle)

        if  self._input_service.is_right_released():
            for obstacle in cast["obstacle"]:
                ebullets = cast["ebullet"]
                position = Point(obstacle.get_position().get_x() - 3, obstacle.get_position().get_y())
                velocity = Point(0, 4)

                ebullet = Ebullets()
                ebullet.set_position(position)
                ebullet.set_velocity(velocity)
                ebullets.append(ebullet)

        if  self._input_service.is_left_released():
            for robstacle in cast["robstacle"]:
                ebulletsp = cast["ebulletp"]
                position = Point(robstacle.get_position().get_x() - 5, robstacle.get_position().get_y())
                velocity = Point(0, 4)

                ebulletp = Ebulletsp()
                ebulletp.set_position(position)
                ebulletp.set_velocity(velocity)
                ebulletsp.append(ebulletp)

        if constants.SCORE >= 15:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(1, constants.BULLET_SPEED)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)

        if constants.SCORE >= 30:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(-1, constants.BULLET_SPEED)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)
         
        if 32 >= constants.SCORE >= 30:
            if self._input_service.is_down_released():
                obstacles = cast["obstacle"]
                x = random.randint(0, 150)
                y = random.randint(0, 75)
                position = Point(x, y)

                dx = 10
                dy = 10
                velocity = Point(dx, dy)

                obstacle = Obstacles()
                obstacle.set_position(position)
                obstacle.set_velocity(velocity)
                obstacles.append(obstacle)

        if  42 >= constants.SCORE >= 40:
            if  self._input_service.is_right_released():
                for obstacle in cast["obstacle"]:
                    ebullets = cast["ebullet"]
                    position = Point(obstacle.get_position().get_x() - 3, obstacle.get_position().get_y())
                    velocity = Point(0, -2)

                    ebullet = Ebullets()
                    ebullet.set_position(position)
                    ebullet.set_velocity(velocity)
                    ebullets.append(ebullet)

            if  self._input_service.is_left_released():
                for robstacle in cast["robstacle"]:
                    ebulletsp = cast["ebulletp"]
                    position = Point(robstacle.get_position().get_x() - 5, robstacle.get_position().get_y())
                    velocity = Point(0, -2)

                    ebulletp = Ebulletsp()
                    ebulletp.set_position(position)
                    ebulletp.set_velocity(velocity)
                    ebulletsp.append(ebulletp)

            
        if constants.SCORE >= 50:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(7, -7)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)

        if 52 >= constants.SCORE >= 50:
            if self._input_service.is_down_released():
                obstacles = cast["obstacle"]
                x = random.randint(0, 150)
                y = random.randint(0, 75)
                position = Point(x, y)

                dx = 10
                dy = 10
                velocity = Point(dx, dy)

                obstacle = Obstacles()
                obstacle.set_position(position)
                obstacle.set_velocity(velocity)
                obstacles.append(obstacle)

        if constants.SCORE >= 100:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(-7, -7)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)

        if constants.SCORE >= 200:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(-7, 7)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)

        if constants.SCORE >= 500:
            if  self._input_service.is_space_released():
                bullets = cast["bullet"]
                position = Point(tank.get_position().get_x() + 8, tank.get_position().get_y())
                velocity = Point(-7, -7)

                bullet = Bullets()
                bullet.set_position(position)
                bullet.set_velocity(velocity)
                bullets.append(bullet)

            if  self._input_service.is_right_released():
                for obstacle in cast["obstacle"]:
                    ebullets = cast["ebullet"]
                    position = Point(obstacle.get_position().get_x() - 3, obstacle.get_position().get_y())
                    velocity = Point(0, -4)

                    ebullet = Ebullets()
                    ebullet.set_position(position)
                    ebullet.set_velocity(velocity)
                    ebullets.append(ebullet)

            if  self._input_service.is_left_released():
                for robstacle in cast["robstacle"]:
                    ebulletsp = cast["ebulletp"]
                    position = Point(robstacle.get_position().get_x() - 5, robstacle.get_position().get_y())
                    velocity = Point(0, -4)

                    ebulletp = Ebulletsp()
                    ebulletp.set_position(position)
                    ebulletp.set_velocity(velocity)
                    ebulletsp.append(ebulletp)