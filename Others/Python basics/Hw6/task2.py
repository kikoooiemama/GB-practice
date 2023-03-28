# Реализовать класс Road (дорога).

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, weight, thickness):
        return round(self._length * self._width * weight * thickness / 1000)


road = Road(20, 5000)
mass = road.calculate_mass(25, 5)
print(f"Масса асфальта: {mass} т.")
