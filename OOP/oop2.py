# магазин с наследованием

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount > self.quantity:
            print(f"Недостаточно {self.name}")
            return False
        self.quantity -= amount
        print(f"Покупка {amount} шт {self.name} оформлена")
        return True

    def show_info(self):
        print(f"{self.name}, цена: {self.price}, количество: {self.quantity}")


class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date): #доп атрибут
        super().__init__(name, price, quantity) # от род класса
        self.expiration_date = expiration_date     # доп атрибут


    def show_expiration(self):
        print(f"Срок годности продукта {self.name}: {self.expiration_date}")

class ElectronicsProduct(Product):
    def __init__(self, name, price, quantity, warranty_years): #доп атрибут
        super().__init__(name, price, quantity) # от род класса
        self. warranty_years =  warranty_years  # доп атрибут

    def show_warranty(self):
        print(f"Срок гарантии продукта {self.name}: {self.warranty_years} год(а)")


hleb = FoodProduct("Хлеб", 100, 10, "10.11.2025")
apple = ElectronicsProduct('Apple pro m4', 22500, 6, 1)
hleb.show_expiration()
apple.show_warranty()
apple.buy(3)
hleb.buy(3)