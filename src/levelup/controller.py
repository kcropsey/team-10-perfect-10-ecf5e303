import logging
from dataclasses import dataclass
from levelup.direction import Direction
from levelup.character import Character
from levelup.map import Map
from levelup.gameStatus import GameStatus


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:
    status: GameStatus
    character: Character
    map: Map

    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        """creates a map, if the char exists adds to map, if char does not exist create new char, and enter map"""
        self.map=Map()
        try:
            self.character
        except AttributeError:
            self.create_character()
        self.character.enter_map(self.map)


    def create_character(self, character_name: str=None) -> None:
        if character_name is None or character_name != "":
            self.character=Character(character_name)
        else:
            raise CharacterNotFoundException("Name must be a valid string")

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class

        self.character.move(direction)
        # TODO: Should probably also update the game results
        pass

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        return self.map.get_total_positions()

    
