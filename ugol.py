class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            print("Ширина должна быть положительной.")

    def get_height(self):
        return self._height

    def set_height(self, height):
        if height > 0:
            self._height = height
        else:
            print("Высота должна быть положительной.")

    def area(self):
        return self._width * self._height


rect = Rectangle(10, 5)
print(f"Начальная площадь: {rect.area()}") # Вывод площади
rect.set_width(15) # Изменение ширины
rect.set_height(7) # Изменение высоты
print(f"Площадь после изменения: {rect.area()}") # Вывод площади

