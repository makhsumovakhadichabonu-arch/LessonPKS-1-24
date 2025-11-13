class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = price
        self._is_booked = False
        self._client = None
        self._days = days 
    
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value>=5000:
            self.__price = value
        else:
            print("цена не может быть ниже 5000 сом")


    def book(self, client): #бронирует тур, делает его недоступным
           if not self._is_booked:
            if client.pay(self.__price):
                self._is_booked = True
                self._client = client
                print(f"Тур {self.__id} успешно забронирован для {client.name}.")
            else:
                print(f"Тур {self.__id} уже забронирован.")     

    def cancel_booking(self): #отменяет бронь, делает тур доступным
        if self._is_booked:
            print(f"Бронь тура {self.__id} отменена для {self._client.name}.")
            self._client.add_balance(self.__price)
            self._is_booked = False
            self._client = None
        else:
            print(f"Тур {self.__id} не забронирован.")

    def info(self): 
        status = "Забронирован" if self._is_booked else "Доступен"
        client_name = self._client.name if self._client else "-"
        print(f"ID: {self.__id}, Цена: {self.__price}, Дней: {self._days}, Статус: {status}, Клиент: {client_name}")

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print(f"{self.name}, недостаточно средств для оплаты тура ({amount} сом)")
            return False
          
    def add_balance(self,amount):
         self.balance += amount
         print(f"{self.name} пополнил баланс на {amount} сом. Текущий баланс: {self.balance} сом.")

    def info(self):
        print(f" Клиент: {self.name}Баланс: {self.balance}сом")



class Agency:
    def __init__(self, name):
        self.name = name 
        self.tours = [] 
        self._income = 0  #доход агентства

    def add_tour(self, tour):
        self.tours.append(tour)
        print(f"Тур {tour.id} добавлен в агенство {self.name}.")


    def show_available_tours(self):
        print("Доступные туры:")
        for tour in self.tours:
            if not tour._is_booked:
                tour.info()

    def book_tour(self, client, tour_id):
       for tour in self.tours:
            if tour.id == tour_id:
                if not tour._is_booked and client.pay(tour.price):
                    tour.book(client)
                    self._income += tour.price
                    return
                elif tour._is_booked:
                    print(f"Тур {tour_id} уже забронирован.")
                    return
                print(f"Тур с ID {tour_id} не найден.")
    def cancel_all_bookings(self):
          for tour in self.tours:
            if tour._is_booked:
                tour.cancel_booking()

    def  show_status(self):
        print(f"Агентство: {self.name}, Доход: {self._income} сом")
        print("Список всех туров:")
        for tour in self.tours:
            tour.info()


if __name__ == "__main__":
    agency = Agency("Sunny Travel")
    tour1 = Tour(1, 6000, 7)
    tour2 = Tour(2, 8000, 10)

    client1 = Client("Алиса", 10000)
    client2 = Client("Боб", 4000)

    agency.add_tour(tour1)
    agency.add_tour(tour2)

    agency.show_available_tours()

    agency.book_tour(client1, 1) 
    agency.book_tour(client2, 2) 
    agency.show_status()

    agency.cancel_all_bookings()
    agency.show_status()

