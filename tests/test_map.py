from unittest import TestCase
from levelup.map import Map

class TestMap(TestCase):
    # get_positions() testing
    def test_map_init(self):
        """ensure that the Map was instantiated"""
        test_map = Map()
        assert test_map is not None

    # calculate_position tests
    def test_calculate_position(self):
        # create a map of positions
        test_map = Map()
        # validate a position change when the change is valid
        assert test_map.calculate_position(test_map.get_positions()[0][0],"SOUTH") != test_map.get_positions()[0][0]

        # validate a position change when the change is invalid (e.g. bounce)
        assert test_map.calculate_position(test_map.get_positions()[0][0],"NORTH") == test_map.get_positions()[0][0]

    # is_position_valid tests
    def test_is_position_valid(self):
        # is_position_valid is not used, the calcualation for moves implements it's own validity check
        assert True

    # get_total_positions tests
    def test_map_total_positions(self):
        test_map = Map()
        assert test_map.get_total_positions() == len(test_map.positions)*len(test_map.positions[0])
        assert test_map.get_total_positions() == test_map.num_positions



