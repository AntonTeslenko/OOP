import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, numeric):
        return Vector(self.x * numeric, self.y * numeric)

    def __lt__(self, other):
        return self.length() < other.length()

    def __eq__(self, other):
        return self.length() == other.length()

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * 3)
print(vector1 < vector2)
print(vector1 == vector2)
print(vector1.length())
