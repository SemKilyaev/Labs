"""Определите класс Apple с четырьмя переменными экземпляра, представляющими
свойства яблока"""
class Apple:
    def __init__(self, w, c, geo, cash):
       self.weight=w
       self.color=c
       self.geolocation=geo
       self.howmatch=cash
       print("Создано")
apl1=Apple(100, "red", "Cuban", 35)
print(apl1)
