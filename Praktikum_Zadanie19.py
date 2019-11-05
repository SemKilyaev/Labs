"""Создайте класс Triangle с методом area, подсчитывающим и возвращающим
площадь треугольника. Затем создайте объект Triangle, вызовите в нем метод
area и выведите результат."""
class Triangle:
    def __init__(self, b, h):
        self.shirina=b
        self.visota=h
    def area(self):
        return (self.shirina*self.visota)/2
triangle1=Triangle(20, 10)
print(triangle1.area())
