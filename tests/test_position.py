from unittest import TestCase
from levelup.position import Position
from levelup.point import Point

class TestPosition(TestCase):
    def test_init(self):
            ARBITRARY_X = 7
            ARBITRARY_Y = 8
            point = Point(7,8)
            testObj = Position(ARBITRARY_X, ARBITRARY_Y)
            self.assertEqual( testObj.coordinates, point)

