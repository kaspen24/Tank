import os

from game.constants import BRICK_WIDTH, MAX_Y
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
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # TODO: Create bricks here and add them to the list
    bricks = []
    for i in range(15, 750, 48):
        for n in range( 0, 200, 24):
            x = i            
            y = n
            position = Point(x, y)

            brick = Brick()
            brick.set_position(position)
            bricks.append(brick)
    cast["brick"] = bricks

    # TODO: Create a ball here and add it to the list
    balls = []
    x = constants.BALL_X         
    y = constants.BALL_Y
    position = Point(x, y)
    #velocity = Point(constants.VELOCITY_DX, constants.VELOCITY_DY)
   
    ball = Ball()
    ball.set_position(position) 
    #ball.set_velocity(velocity)
    balls.append(ball)
    cast["balls"] = [ball]

    # TODO: Create a paddle here and add it to the list
    paddles = []
    x = constants.PADDLE_X          
    y = constants.PADDLE_Y
    position = Point(x, y)

    paddle = Paddle()
    paddle.set_position(position)
    paddles.append(paddle)
    cast["paddle"] = paddles
   
    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_off_screen_action = HandleOffScreenAction()

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
