from levelup.position import Position
from levelup.point import Point

class Map:
    dirmap={
        "NORTH" : ['y',-1],
        "SOUTH" : ['y',1],
        "EAST" : ['x',1],
        "WEST" : ['x',-1]
    }

    def __init__(self):
        self.max_x = 10
        self.max_y = 10
        #Position is created by passing xcoord, ycoord, position is returned with a point containing coords
        self.positions=[]
        for x in range(self.max_x):
            self.positions.append([])
            for y in range(self.max_y):
                self.positions[x].append(Position(x,y))
        self.starting_position=self.positions[0][0]
        self.num_positions = len(self.positions)*len(self.positions[0])
        self.dirmap={
            "NORTH" : ['y',-1],
            "SOUTH" : ['y',1],
            "EAST" : ['x',1],
            "WEST" : ['x',-1]
        }
        self.calculate_position(self.positions[0][0],"SOUTH")

    def get_positions(self):
        return self.positions

    def calculate_position(self, current_position, direction):
        """Based on direction given, attempt to return a new position based on direction"""
        # attempt to get a position with coordinates modified based on direction
        if self.dirmap[direction][0] == 'x':
            # compare the east/west direction against x value in current_position
            # if the current_position would go out of bounds, return current_position
            # otherwise, return position with adjusted coordinate.
            if current_position.coordinates.x + self.dirmap[direction][1] >= 0 and current_position.coordinates.x + self.dirmap[direction][1] < self.max_x:
                return self.positions[current_position.coordinates.x + self.dirmap[direction][1]][current_position.coordinates.y]
            else:
                return current_position
        elif self.dirmap[direction][0] == 'y':
            if current_position.coordinates.y + self.dirmap[direction][1] >= 0 and current_position.coordinates.y + self.dirmap[direction][1] < self.max_y:
                return self.positions[current_position.coordinates.x][current_position.coordinates.y + self.dirmap[direction][1]]
            else:
                return current_position
        return

    def is_position_valid(self, position_coordintaes):
        """Not implemented - tests for validity are builtin to the calculate_position function."""
        return True

    def get_total_positions(self):
        return 42
