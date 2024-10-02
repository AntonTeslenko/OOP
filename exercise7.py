class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(self.components[0] + other.components[0],
                                  self.components[1] + other.components[1],
                                  self.components[2] + other.components[2])

    def __sub__(self, other):
        return Vector(self.components[0] - other.components[0],
                                  self.components[1] - other.components[1],
                                  self.components[2] - other.components[2])

    def __mul__(self, other):
        return (self.components[0] * other.components[0]
                + self.components[1] * other.components[1]
                + self.components[2] * other.components[2])

    def __repr__(self):
        return f"Vector{self.components}"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)


# Додавання векторів
v3 = v1 + v2
print("Сума векторів: ", v3)

# Віднімання векторів
v4 = v1 - v2
print("Різниця векторів: ", v4)

# Скалярний добуток
v5 = v1 * v2
print("Скалярний добуток: ", v5)

