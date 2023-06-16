class Point(tuple):
            def __new__(self, x, y):
                        point = tuple.__new__(Point, (x, y))
                        point.x = x
                        point.y = y
                        return point