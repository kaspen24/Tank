import os

from game.constants import OBSTACLE_WIDTH, MAX_Y
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\Kaden Spencer\myproject\cse210-student-solo-checkpoints-1\07-snake\raylib-2.0.0-Win64-mingw\raylib-2.0.0-Win64-mingw\lib'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService

# TODO: Add imports similar to the following when you create these classes
from game.tank import Tank
from game.obstacles import Obstacles
from game.robstacles import Robstacles
from game.bullets import Bullets
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # TODO: Create a Tank here and add it to the list
    tanks = []
    x = 400     
    y = 300
    position = Point(x, y)

    tank = Tank()
    tank.set_position(position)
    tanks.append(tank)
    cast["tank"] = tanks

    # TODO: Create a Obstacles here and add it to the list
    obstacles = []
    for n in range(15):

        x = random.randint(0, 300)
        y = random.randint(0, 200)
        position = Point(x, y)

        dx = random.uniform(0, constants.VELOCITY_DX)
        dy = random.uniform(0, constants.VELOCITY_DY)
        velocity = Point(dx, dy)

        obstacle = Obstacles()
        obstacle.set_position(position)
        obstacle.set_velocity(velocity)
        obstacles.append(obstacle)
    cast["obstacle"] = obstacles

    robstacles = []
    for n in range(15):

        x = random.randint(600, 800)
        y = random.randint(500, 600)
        position = Point(x, y)

        dx = random.uniform(0, constants.RVELOCITY_DX)
        dy = random.uniform(0, constants.RVELOCITY_DY)
        velocity = Point(dx, dy)

        robstacle = Robstacles()
        robstacle.set_position(position)
        robstacle.set_velocity(velocity)
        robstacles.append(robstacle)
    cast["robstacle"] = robstacles
   
   # TODO: Create a Bullets here and add it to the list
    bullets = []
    position = tank.get_position()
    velocity = Point(0, constants.VELOCITY_DX)

    bullet = Bullets()
    bullet.set_position(position)
    bullet.set_velocity(velocity)
    bullets.append(bullet)
    cast["bullet"] = bullets

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Tank");
    director = Director(cast, script)
    director.start_game()

if __name__ == "__main__":
    main()
