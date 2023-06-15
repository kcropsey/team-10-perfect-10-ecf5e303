class Map:
    positions=[ [0]*10 for i in range(10)]
    starting_position=(0,0)
    num_positions = 100

    def __init__(self):
        positions=[ [0]*10 for i in range(10)]
        starting_position=(0,0)
        num_positions = len(positions)*len(positions[0])

    def get_positions(self):
        return self.positions

    def calculate_position(self, starting_position, direction):
        return

    def is_position_valid(self, position_coordintaes):
        return True

    def get_total_positions(self):
        return 42
