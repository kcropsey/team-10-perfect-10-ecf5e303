from unittest import TestCase
from levelup.controller import GameController
from fake_character import FakeCharacter
from levelup.direction import Direction

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None

    def test_move(self):
        testObj = GameController()
        character = FakeCharacter("Kim")
        currentPosition = character.current_position
        character.move(Direction.NORTH)
        newPosition = character.current_position
        self.assertTrue(character.is_move_called)
        self.assertEqual(character.last_move_direction, Direction.NORTH)
        

        
