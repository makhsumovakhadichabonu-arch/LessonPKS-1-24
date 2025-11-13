class Client:
    def __init__(self, name, balance=0, discount=0):
        self.name = name
        self._balance = balance
        self._discount = discount

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не может быть отрицательным!")
        else:
            self._balance = value

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if value < 0:
            print("Скидка не может быть отрицательной!")
        elif value > 30:
            print("Скидка не может превышать 30%!")
        else:
            self._discount = value

    def add_balance(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.name} пополнил баланс на {amount}")
        else:
            print("Сумма пополнения должна быть положительной")

    def pay(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        else:
            print(f"Недостаточно средств! Баланс: {self._balance}")
            return False

    def info(self):
        print(f"Клиент: {self.name}, Баланс: {self._balance}, Скидка: {self._discount}%")




class Hotel:
    def __init__(self, name, city, price_per_night, stars):
        self.name = name
        self.city = city
        self._price_per_night = price_per_night
        self._stars = stars

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value < 1000:
            print("Цена за ночь не может быть меньше 1000 сом")
        else:
            self._price_per_night = value

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        if 1 <= value <= 5:
            self._stars = value
        else:
            print("Звезды должны быть от 1 до 5")

    def info(self):
        print(f"Отель: {self.name}, Город: {self.city}, Цена за ночь: {self._price_per_night}, Звезды: {self._stars}")




class Tour:
    def __init__(self, destination, hotel, days, base_price, available=True):
        self.destination = destination
        self.hotel = hotel
        self.days = days
        self.base_price = base_price
        self._available = available

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value
        if not value:
            print(f"Тур в {self.destination} закрыт для бронирования")

    def calculate_total_price(self, client):
        hotel_total = self.hotel.price_per_night * self.days
        discount_amount = (self.base_price + hotel_total) * (client.discount / 100)
        total_price = self.base_price + hotel_total - discount_amount
        return total_price

    def info(self):
        status = "Доступен" if self._available else "Закрыт"
        print(f"Тур: {self.destination}, Отель: {self.hotel.name}, Дней: {self.days}, Базовая цена: {self.base_price}, Статус: {status}")



class Booking:
    def __init__(self, client, tour):
        self.client = client
        self.tour = tour
        self._paid = False

    def make_payment(self):
        price = self.tour.calculate_total_price(self.client)
        if self.client.pay(price):
            self._paid = True
            print(f"{self.client.name} оплатил тур в {self.tour.destination} на сумму {price:.2f}")
        else:
            print(f"Оплата не выполнена для {self.client.name}")

    def info(self):
        status = "Оплачен" if self._paid else "Не оплачен"
        print(f"Бронь: Клиент {self.client.name}, Тур {self.tour.destination}, Статус: {status}")

class Agency:
    def __init__(self, name):
        self.name = name
        self.tours = []
        self.clients = []
        self._income = 0
        self.bookings = []

    def add_tour(self, tour):
        self.tours.append(tour)
        print(f"Тур в {tour.destination} добавлен")

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен")

    def book_tour(self, client_name, destination):
        client = next((c for c in self.clients if c.name == client_name), None)
        tour = next((t for t in self.tours if t.destination == destination), None)

        if client and tour:
            if not tour.available:
                print(f"Тур {destination} недоступен для бронирования")
                return
            booking = Booking(client, tour)
            booking.make_payment()
            self.bookings.append(booking)
            if booking._paid:
                self._income += tour.calculate_total_price(client)
        else:
            print("Клиент или тур не найден")

    def show_tours(self):
        print("\nСписок туров:")
        for t in self.tours:
            t.info()

    def show_clients(self):
        print("\nСписок клиентов:")
        for c in self.clients:
            c.info()

    def calculate_income(self):
        print(f"\nОбщий доход агентства: {self._income:.2f}")
        return self._income

    def top_destination(self):
        destinations = {}
        for b in self.bookings:
            if b._paid:
                destinations[b.tour.destination] = destinations.get(b.tour.destination, 0) + 1
        if destinations:
            top = max(destinations, key=destinations.get)
            print(f"Самое популярное направление: {top} ({destinations[top]} брони)")
        else:
            print("Брони пока нет")

if __name__ == "__main__":
    agency = Agency("TravelGuru")

    client1 = Client("Хадичабону", balance=50000, discount=10)
    client2 = Client("Айжамал", balance=30000, discount=5)
    agency.add_client(client1)
    agency.add_client(client2)

    hotel1 = Hotel("Sunrise", "Бишкек", 2000, 4)
    hotel2 = Hotel("MountainView", "Нарын", 1500, 3)

    tour1 = Tour("Бишкек", hotel1, days=3, base_price=10000)
    tour2 = Tour("Нарын", hotel2, days=2, base_price=8000)
    agency.add_tour(tour1)
    agency.add_tour(tour2)

    agency.book_tour("Хадичабону", "Бишкек")
    agency.book_tour("Айжамал", "Нарын")

    agency.show_clients()
    agency.show_tours()
    agency.calculate_income()
    agency.top_destination()
