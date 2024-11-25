import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius*2

    def set_diameter(self, diameter):
        self.radius = diameter / 2


circle = Circle(5)
print(f"Начальная площадь: {circle.area()}")
circle.set_diameter(10) # Изменение радиуса через диаметр
print(f"Площадь после изменения диаметра: {circle.area()}") # Площадь круга
