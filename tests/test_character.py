from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_init_default(self):
        testobj = Character()
        self.assertEqual(testobj.default_name, testobj.name)

    def test_enter_map(self):
        map = {}
        testobj = Character()
        testobj.enter_map(map)
        self.assertEqual(testobj.map, map)
