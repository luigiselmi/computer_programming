import math

def add(a, b):
    return a + b

class Point:
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
        