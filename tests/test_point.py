from unittest import TestCase
from levelup.point import Point

class TestPointInitWithCoordinates(TestCase):
    def test_init(self):
        ARBITRARY_X = 4
        ARBITRARY_Y = 8
        testobj = Point(ARBITRARY_X, ARBITRARY_Y)
        
        self.assertEqual(ARBITRARY_X, testobj.x)
        self.assertEqual(ARBITRARY_Y, testobj.y)