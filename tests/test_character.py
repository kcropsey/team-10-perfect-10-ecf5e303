from unittest import TestCase
from levelup.character import Character

class TestMap():
    starting_position = {}
    has_calculated_position = False

    def calculatePosition(self, position, direction):
        self.has_calculated_position = True
        return position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_init_default(self):
        testobj = Character()
        self.assertEqual(testobj.default_name, testobj.name)

    def test_enter_map(self):
        map = TestMap()

        testobj = Character()
        testobj.enter_map(map)
        self.assertEqual(testobj.map, map)
        self.assertEqual(testobj.position, map.starting_position)

    def test_move(self):
        map = TestMap()

        testobj = Character()
        testobj.enter_map(map)
        start_move_count = testobj.move_count
        start_position = testobj.position
        testobj.move("NORTH")
        # Move count incremented
        self.assertEqual(start_move_count + 1, testobj.move_count)
        # The position is still a position
        self.assertEqual(type(start_position), type(testobj.position))
        # TestMap has been called
        self.assertTrue(map.has_calculated_position)