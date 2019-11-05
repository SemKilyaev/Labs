"""Создайте класс Hexagon с методом calculate_perimetre, подсчитывающим и
возвращающим периметр шестиугольника. Затем создайте объект Hexagon, вызовите
в нем метод calculate_perimetre и выведите результат."""
class Hexagon:
    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.long1=a1
        self.long2=a2
        self.long3=a3
        self.long4=a4
        self.long5=a5
        self.long6=a6
        print('Ready')
    def calculate_perimetre(self):
        if self.long1==self.long2==self.long3==self.long4==self.long5==self.long6:
            return self.long1*6
        else:
            return self.long1+self.long2+self.long3+self.long4+self.long5+self.long6
        
hexagon1=Hexagon(20, 20, 20, 20, 20, 20)
print(hexagon1.calculate_perimetre())
        
        
        
    
