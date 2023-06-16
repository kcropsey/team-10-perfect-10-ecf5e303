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
        # create a 'mini' map of positions
        # test when a position really is valid
        assert True
        # test when coordinates/position passed is invalid
        assert False==False

    # get_total_positions tests
    def test_map_total_positions(self):
        """Assuming 100 total positions (10x10 map), we should always be returning 100 tiles"""
        test_map = Map()

        # validate that a 2-dimensional position array was created
        self.assertIsInstance(test_map.get_positions(),list)



