# ЗАДАЧА: Cистема книжного магазина
# Требуется реализовать систему управления книжным магазином с использованием инкапсуляции, наследования, аргументов *args и **kwargs.
# класс BaseBook:
# защищённые атрибуты: _title, _author
# приватный атрибут: __price
# свойство price с проверкой (цена ≥ 100)
# абстрактный метод info()
# Классы-наследники от BaseBook:
# • Book — обычная книга. Реализация info(): «Книга: <title> — <author>, <price> сом»
# • EBook — электронная книга. Доп. атрибут: _file_size_mb. info(): «Электронная книга: <title> — <author>, <price> сом, файл <size> МБ»
# • AudioBook — аудиокнига. Доп. атрибут: _duration_min. info(): «Аудиокнига: <title> — <author>, <price> сом, длительность <minutes> мин»
# Класс Inventory (склад):
# защищённый список _books
# метод add_books(*books): принимает любое количество объектов книг, проверяет тип
# метод find_books(**filters): возвращает список книг, соответствующих переданным параметрам
# метод remove_book(book): удаляет книгу
# метод all_books(): возвращает копию списка книг
# Класс BookStore:
# атрибут name
# объект inventory
# приватный атрибут __income + свойство income (только чтение)
# метод sell_book(title): ищет по названию, удаляет книгу, увеличивает доход
# метод show_status(): возвращает название магазина, доход и список всех книг через info()
# Требования:
# обязательно использовать инкапсуляцию (__ и _), наследование, полиморфизм, *args, **kwargs
# система должна демонстрировать добавление книг, поиск, продажу и отображение состояния магазина

from abc import ABC, abstractmethod
from copy import deepcopy

class BaseBook:
    def __init__(self, title, author, price):
        self._title =  title
        self._author = author
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value >= 100:
            self.__price = value

    
    def info(self):
        return f"{self.title} {self._author} {self.price}"
        

    
class Book(BaseBook):
    def info(self):
        return f"Книга: {self._title} — {self._author}, {self.price} сом"

class EBook(BaseBook):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self._file_size_mb = file_size_mb  

    def info(self):
        return f"Электронная книга: {self._title} - {self._author}, {self.price} сом, файл {self._file_size_mb} МБ"


class AudioBook(BaseBook):
    def __init__(self, title, author, price, duration_min):
        super().__init__(title, author, price)
        self._duration_min = duration_min  

    def info(self):
       return f"Аудиокнига: {self._title} — {self._author}, {self.price} сом, длительность {self._duration_min} мин"


class Inventory:
    def __init__(self):
        self._books = []

    def add_books(self, *books):
        for book in books:
            if not isinstance(book, BaseBook):
                raise TypeError("Можно добавлять только объекты книг")
        self._books.append(book)


    def find_books(self, **filters):
        result = []
        for book in self._books:
            match = True
            for attr, value in filters.items():
                if not hasattr(book, f"_{attr}") and not hasattr(book, attr):
                    match = False
                    break
                
                if getattr(book, f"_{attr}", getattr(book, attr, None)) != value:
                    match = False
                    break
            if match:
                result.append(book)
        return result

    def remove_book(self, book):
        if book in self._books:
            self._books.remove(book)

    def all_books(self):
        return deepcopy(self._books)  
    
class BookStore:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.__income = 0  

    @property
    def income(self):
        return self.__income  

    def sell_book(self, title):
        books = self.inventory.find_books(title=title)
        if books:
            book = books[0]
            self.inventory.remove_book(book)
            self.__income += book.price
            return book
        else:
            print(f"Книга с названием '{title}' не найдена.")
            return None

    def show_status(self):
        print(f"Магазин: {self.name}")
        print(f"Доход: {self.income} сом")
        print("Все книги:")
        for book in self.inventory.all_books():
            print(" -", book.info())

if __name__ == "__main__":
    b1 = Book("Война и мир", "Толстой", 500)
    b2 = EBook("Python для всех", "Смит", 300, 5)
    b3 = AudioBook("Шерлок Холмс", "Дойл", 400, 600)

    store = BookStore("Книжный мир")

    store.inventory.add_books(b1, b2, b3)

    store.show_status()
    print("\nПродаём книгу 'Python для всех'...\n")
    store.sell_book("Python для всех")  

    store.show_status()



    