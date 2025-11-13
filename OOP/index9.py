# ООП - обьектно-ориенторавнное программирование
#         Наследование
#         Инкапсуляция
#         Полиморфизм
#         Абстракция
class Cat: # Название класса
        def __init__(self, name, age): # конструктор класса 
                # магические метод init через два нижних подчеркивания с начала и в конце, обязательно внутри скобок self 
                self.name = name # атрибуты класса
                self.age = age # атрибуты класса

        def info(self):
            return f"{self.name} {self.age}"
        
cat1 = Cat ('Felix', 2) # создание экземепляра / экземпляр класса 
# print(cat1.info())
######################
car1_brand = 'Toyota'
car1_year = 2020
car2_brand = 'Kia'
car2_year = 2018

def start_car(brand, year):
       print(f"{brand} стартанула, а она {year}")

start_car(car1_brand, car1_year)
start_car(car2_brand, car2_year)
######### ООП пример 
class Car:
       def __init__(self, brand, year, speed):
              self.brand = brand
              self.year = year
              self.speed = speed
              self.is_going = False

       def car_is_start(self, kmH): # методы класса
              self.speed += kmH
              self.is_going = True

       def car_is_stop(self):
              self.speed = 0
              self.is_going = False
              
       def info(self):
              print(f"Бренд: {self.brand} Год: {self.year} Скорость:{self.speed}km/h, Идет: {self.is_going}")
            
car1 = Car('BMW', 2022, 0)
car1.car_is_start(50)
car1.car_is_start(20)
car1.info()