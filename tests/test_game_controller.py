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
        testObj.character = character
        currentPosition = character.current_position
        testObj.move(Direction.NORTH)
        newPosition = character.current_position
        self.assertTrue(character.is_move_called)
        #self.assertEqual(character.last_move_direction, Direction.NORTH)

    def test_create_character(self):
        test_char="TestChar"
        testObj = GameController()
        testObj.create_character(test_char)
        assert test_char == testObj.character.name

    def test_start_game(self):
        testObj = GameController()
        testObj.start_game()
        #map exists
        assert testObj.map is not None
        #character is put on board
        assert testObj.character.position is not None

    def test_get_status(self):
        assert True

    def test_get_total_positions(self):
        testObj = GameController()
        testObj.start_game()
        assert testObj.map.get_total_positions() == testObj.get_total_positions()
        

        
