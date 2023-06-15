class Point(tuple):
            x: int
            Y: int
            def __new__(self, x, y):
                        self.x = x
                        self.y = y
                        return tuple.__new__(Point, (x, y))