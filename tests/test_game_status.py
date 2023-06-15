from unittest import TestCase
from levelup.gameStatus import GameStatus

class TestGameStatusInit(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "Marco"
#         ARBITRARY_POSITION = new Point(4,8)
        testobj = GameStatus(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.character_name)
