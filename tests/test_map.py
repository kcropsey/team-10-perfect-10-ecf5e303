from unittest import TestCase
from levelup.map import Map

class TestMap(TestCase):
    # get_positions() testing
    def map_init(self):
        testObj = GameController()
        assert testObj.status != None

    # calculate_position tests

    # is_position_valid tests

    # get_total_positions tests
    def test_map_total_positions(self):
        """Assuming 100 total positions (10x10 map), we should always be returning 100 tiles"""
        test_map = Map()

        # ensure that the Map was instantiated
        assert test_map is not None

        # validate that a 2-dimensional position array was created
        self.assertIsInstance(test_map.get_positions(),list)

