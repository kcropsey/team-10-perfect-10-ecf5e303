from unittest import TestCase
from levelup.map import Map

class TestMap(TestCase):
    # get_positions() testing
    def test_map_init(self):
        """ensure that the Map was instantiated"""
        test_map = Map()
        assert test_map is not None

    # calculate_position tests

    # is_position_valid tests

    # get_total_positions tests
    def test_map_total_positions(self):
        """Assuming 100 total positions (10x10 map), we should always be returning 100 tiles"""
        test_map = Map()
        
        # validate that a 2-dimensional position array was created
        self.assertIsInstance(test_map.get_positions(),list)

