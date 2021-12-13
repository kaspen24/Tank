from time import sleep

import raylibpy
from game.output_service import OutputService
output_service = OutputService()

class Director:
    """The responsibility of this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""

        print("")
        print("")
        print("")
        print (f"\033[1;32m DONT LET THE ENEMY TANKS OR BOMBS HIT YOU!")
        print (f"REACHING A SCORE OF 15, 30, 50, 100, 200, and 500 WILL RESULT IN A LEVEL UP")
        print ("")
        print ("")
        print("")
            
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")


            if raylibpy.window_should_close():
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)