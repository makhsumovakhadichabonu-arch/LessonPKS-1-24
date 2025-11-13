# Инкапсуляция - изолируюм обьект 
#         public - публичный
#         _protected - защищены
#         __private - приватный
class Animal:  # Родительский класс
    def __init__(self, name, age, color, gender):
        self.name = name
        self.__age = age
        self.color = color
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 20:
            self.__age = value
        else:
            print("Возраст должен быть от 1 до 19 лет.")

    def info(self):
        print(f'Имя: {self.name}, Возраст: {self.__age}, Цвет: {self.color}, Гендер: {self.gender}')

    def set_name(self, new_name):
        self.name = new_name
        return self.name


class Cat(Animal):
    def mau(self):
        print("Мяу-мяу!")


class Dog(Animal):
    def gav(self):
        print("Гав-гав!")


cat1 = Cat('Felix', 2, 'рыжий', 'самка')
dog1 = Dog('Bobik', 3, 'черный', 'самец')

cat1.mau()
cat1.set_name('Мурка')
cat1.info()

dog1.set_name('Шарик')
dog1.info()
dog1.gav()
