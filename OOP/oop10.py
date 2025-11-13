# *args - arguments
def  add(*args):
    total = 0
    for i in args:
        total+=i
    print(total)
add(4,4,4,3,4,5,6,7,7)

################  **kwargs - keyword arguments
def pets(owner, **kwargs):
    print(owner)
    for k,v in kwargs.items():
        print(k,v)

pets( 'Aliya', cat='Felix', dog='Bobik', city='Bishkek', age=18)

##### Комбинация
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(7703010101, 180, 90,name="Gena", prof="Слесарь")
###
class Student:
    def __init__(self, name, kwargs):
        self.name = name
        self.kwargs = kwargs

    def info(self):
        print(f"name: {self.name}")
        for i,v in self.kwargs.items():
            print(f"{i},{v}")

        s = Student('Oleg', car='Gelik', home="JK Muras", children="Vanya")
        s.info()

my_str = 'rgr4fef45ferfe567rgfrgr6789'
nums = []
digits = ''.join([ch for ch in my_str if ch.isdigit()])

nums.append(digits[0])
nums.append(digits[1:3])
nums.append(digits[3:6])
nums.append(digits[6:])

print(nums)

import re #егулярные выражения
nums = []  
my_str = 'rgr4fef45ferfe567rgfrgr6789'
numbers = re.findall('[0-9]+', my_str)
for i in numbers:
    nums.append(int(i))
print(nums)


def fh():
    print("Привет ребята")

hello = fh # функция это обьект 
hello()
#№№№№№№№№
def gromko(text):
    return text.upper()

def tiho(text):
    return text.lower()

def speak(func,x):
    res = func(x)
    return res

print(speak(gromko, 'как дела гена'))
print(speak(tiho, 'Хорошо Вася, сам как'))

##### функция передаем как параметр, и она работает внутри другой
def inc(x):
    return x*2

def dec(x):
    return x/2

def oper(func, x):
    res = func(x)
    return res

print(oper(inc, 6))
print(oper(inc, 9))
##########
def before_after(func):
    def wrapper():
        print("то что может работать до")
        func()
        print("то что может работать после")
    return wrapper

@before_after
def say_hi():
    print("привет друг")

decorated = before_after(say_hi)
decorated()
say_hi()


@property
# getter
# setter
# deleter

class Teacher:
    def __init__(self, name, phone):
        self.name = name
        self.__phone = phone

    @property # мы обрашаемся к методам как к атрибутам,
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        print("Сеттер сработал")
        self.__phone = value

    @phone.deleter
    def phone(self):
        print('Удалили номер deleter')
        del self.__phone

    def info(self):
        return f"{self.name} {self.__phone}"
    
t = Teacher('Ali', 770770770)
t.phone = 45
print(t.phone)
#del t.phone
print(t.info())