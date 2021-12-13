import os

from game.constants import OBSTACLE_WIDTH, MAX_Y
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\Kaden Spencer\myproject\cse210-student-solo-checkpoints-1\07-snake\raylib-2.0.0-Win64-mingw\raylib-2.0.0-Win64-mingw\lib'

from game import constants
from game.director import Director
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

from game.tank import Tank
from game.background import Background
from game.border import Border
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction

def main():

    cast = {}

    backgrounds = []
    x = 0
    y = 0 
    position = Point(x, y)

    background = Background()
    background.set_position(position)
    backgrounds.append(background)
    cast["background"] = backgrounds

    borders = []
    x = 0
    y = 595
    position = Point(x, y)  
  
    border = Border()   
    border.set_position(position)
    borders.append(border)
    cast["border"] = borders

    tanks = []
    x = 360    
    y = 275
    position = Point(x, y)

    tank = Tank()
    tank.set_position(position)
    tanks.append(tank)
    cast["tank"] = tanks

    obstacles = []
    cast["obstacle"] = obstacles

    robstacles = []
    cast["robstacle"] = robstacles
   
    bullets = []
    cast["bullet"] = bullets

    ebullets = []
    cast["ebullet"] = ebullets

    ebulletsp = []
    cast["ebulletp"] = ebulletsp

    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    output_service.open_window("Tank")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
