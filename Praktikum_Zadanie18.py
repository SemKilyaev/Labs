"""Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь
круга. Затем создайте объект Circle, вызовите в нем метод area и выведите
результат. Воспользуйтесь функцией pi из встроенно в Python модуля math."""
import math 
class Circle:
    def __init__(self, a, R):
        self.pi=a
        self.radius=R
    def area(self):
        return self.pi*(self.radius**2)
circle1=Circle(math.pi, 20)
print(circle1.area())
        
