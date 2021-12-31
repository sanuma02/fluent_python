from math import hypot 

class Vector:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    
    def __add__(self, to_add):
        _a = self.a + to_add.a
        _b = self.b + to_add.b
        return Vector(_a, _b)
    
    def __mul__(self, multiplier):
        _a = self.a * multiplier
        _b = self.b * multiplier
        return Vector(_a, _b)

    def __repr__(self):
        _r = 'Vector (a:{}, b:{})'.format(self.a, self.b)
        return _r

v = Vector(9, 12)
g = Vector(3, 4)
print(v)
print(v*4)
print(v+g)
