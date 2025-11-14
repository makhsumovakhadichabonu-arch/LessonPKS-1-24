from copy import deepcopy

class Ingredient:
    def __init__(self, name, quantity, price_per_gram):
        self._name = name              
        self._quantity = quantity     
        self.__price_per_gram = None   
        self.price_per_gram = price_per_gram  

    @property
    def price_per_gram(self):
        return self.__price_per_gram

    @price_per_gram.setter
    def price_per_gram(self, value):
        if value >= 0.1:
            self.__price_per_gram = value
        else:
            raise ValueError("Цена за грамм ≥ 0.1")

    def cost(self, weight):
        return weight * self.__price_per_gram

class Dish:
    def __init__(self, name, ingredients: dict, base_price):
        self._name = name
        self._ingredients = ingredients
        self.__base_price = None
        self.base_price = base_price

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, value):
        if value >= 20:
            self.__base_price = value
        else:
            raise ValueError("Минимальная цена блюда ≥ 20 сом")

    def total_cost(self):
        ingredients_cost = sum(ing.cost(weight) for ing, weight in self._ingredients.items())
        return ingredients_cost + self.__base_price

    def info(self):
        return f"{self._name}, цена: {self.total_cost()} сом"

class HotDish(Dish):
    def __init__(self, name, ingredients, base_price, spicy_level):
        super().__init__(name, ingredients, base_price)
        self._spicy_level = spicy_level  

    def info(self):
        return f"Горячее блюдо: {self._name}, острота {self._spicy_level}, цена {self.total_cost()} сом"

class Dessert(Dish):
    def __init__(self, name, ingredients, base_price, sweetness):
        super().__init__(name, ingredients, base_price)
        self._sweetness = sweetness  

    def info(self):
        return f"Десерт: {self._name}, сладость {self._sweetness}, цена {self.total_cost()} сом"

class Drink(Dish):
    def __init__(self, name, ingredients, base_price, volume_ml):
        super().__init__(name, ingredients, base_price)
        self._volume_ml = volume_ml

    def info(self):
        return f"Напиток: {self._name}, объем {self._volume_ml} мл, цена {self.total_cost()} сом"

class Kitchen:
    def __init__(self):
        self._dishes = []

    def add_dishes(self, *dishes):
        for dish in dishes:
            if not isinstance(dish, Dish):
                raise TypeError("Можно добавлять только объекты Dish")
            self._dishes.append(dish)

    def find_dishes(self, **filters):
        found = []
        for dish in self._dishes:
            match = True
            for key, value in filters.items():
                if hasattr(dish, f"_{key}"):
                    attr_val = getattr(dish, f"_{key}")
                elif hasattr(dish, key):
                    attr_val = getattr(dish, key)
                else:
                    match = False
                    break
                if attr_val != value:
                    match = False
                    break
            if match:
                found.append(dish)
        return found

    def remove_dish(self, dish):
        if dish in self._dishes:
            self._dishes.remove(dish)

    def all_dishes(self):
        return deepcopy(self._dishes)  

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.kitchen = Kitchen()
        self.__income = 0

    @property
    def income(self):
        return self.__income

    def order_dish(self, dish_name):
        dishes = self.kitchen.find_dishes(name=dish_name)
        if dishes:
            dish = dishes[0]
            self.kitchen.remove_dish(dish)
            self.__income += dish.total_cost()
            return dish
        else:
            print(f"Блюдо '{dish_name}' не найдено")
            return None

    def menu(self):
        print(f"Меню ресторана {self.name}:")
        for dish in self.kitchen.all_dishes():
            print(" -", dish.info())

    def status(self):
        print(f"Доход: {self.income} сом")
        print(f"Осталось блюд: {len(self.kitchen.all_dishes())}")

if __name__ == "__main__":
    rice = Ingredient("Рис", 1000, 0.5)
    chicken = Ingredient("Курица", 500, 2)
    sugar = Ingredient("Сахар", 200, 0.3)
    milk = Ingredient("Молоко", 1000, 0.4)

    dish1 = HotDish("Плов", {rice: 200, chicken: 150}, 50, spicy_level=3)
    dish2 = Dessert("Торт", {sugar: 50, milk: 200}, 40, sweetness=8)
    dish3 = Drink("Молочный коктейль", {milk: 300, sugar: 20}, 25, volume_ml=250)
    rest = Restaurant("Вкусняшка")

    rest.kitchen.add_dishes(dish1, dish2, dish3)

    rest.menu()
    print("\nЗаказываем блюдо 'Плов'...\n")
    rest.order_dish("Плов")

    rest.status()




    