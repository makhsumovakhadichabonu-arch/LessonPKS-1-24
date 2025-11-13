# Задача: Система авиабронирования
# Создай программу, используй классы, инкапсуляцию и взаимодействие объектов.
# Программа должна позволять: добавлять и удалять рейсы, покупать и отменять билеты, изменять параметры рейса, рассчитывать общую выручку, показывать статистику.
# Класс Flight: Отвечает за конкретный рейс. Содержит: направление (route), количество мест эконом и бизнес, цены,количество проданных билетов,методы для продажи, отмены и изменения данных.
# Класс Airline: Управляет всеми рейсами: список (или словарь) всех рейсов, методы добавления, удаления, поиска и статистики.
# Класс Client, Сохраняет данные клиента и купленного билета.

class Flight:
    def __init__(self, route, seats_economy, seats_business, price_economy, price_business):
        self.__route = route
        self.__seats_economy = seats_economy
        self.__seats_business = seats_business
        self.__price_economy = price_economy
        self.__price_business = price_business
        self.__sold_economy = 0
        self.__sold_business = 0

    def sell_ticket(self, ticket_type, quantity=1):
        if ticket_type == "economy":
            if self.__sold_economy + quantity <= self.__seats_economy:
                self.__sold_economy += quantity
                print(f"{quantity} билет(ов) эконом-класса продано.")
            else:
                print("Недостаточно мест в эконом-классе!")
        elif ticket_type == "business":
            if self.__sold_business + quantity <= self.__seats_business:
                self.__sold_business += quantity
                print(f"{quantity} билет(ов) бизнес-класса продано.")
            else:
                print("Недостаточно мест в бизнес-классе!")
        else:
            print("Неверный тип билета!")

    def cancel_ticket(self, ticket_type, quantity=1):
        if ticket_type == "economy":
            if self.__sold_economy >= quantity:
                self.__sold_economy -= quantity
                print(f"{quantity} билет(ов) эконом-класса отменено.")
            else:
                print("Нельзя отменить больше билетов, чем продано!")
        elif ticket_type == "business":
            if self.__sold_business >= quantity:
                self.__sold_business -= quantity
                print(f"{quantity} билет(ов) бизнес-класса отменено.")
            else:
                print("Нельзя отменить больше билетов, чем продано!")
        else:
            print("Неверный тип билета!")

    def change_parameters(self, seats_economy=None, seats_business=None, price_economy=None, price_business=None):
        if seats_economy is not None:
            self.__seats_economy = seats_economy
        if seats_business is not None:
            self.__seats_business = seats_business
        if price_economy is not None:
            self.__price_economy = price_economy
        if price_business is not None:
            self.__price_business = price_business

    def get_revenue(self):
        return self.__sold_economy * self.__price_economy + self.__sold_business * self.__price_business

    def get_info(self):
        return {
            "route": self.__route,
            "economy_seats": self.__seats_economy,
            "business_seats": self.__seats_business,
            "sold_economy": self.__sold_economy,
            "sold_business": self.__sold_business,
            "price_economy": self.__price_economy,
            "price_business": self.__price_business
        }


class Airline:
    def __init__(self):
        self.__flights = {}

    def add_flight(self, flight_id, flight):
        self.__flights[flight_id] = flight
        print(f"Рейс {flight_id} добавлен.")

    def remove_flight(self, flight_id):
        if flight_id in self.__flights:
            del self.__flights[flight_id]
            print(f"Рейс {flight_id} удален.")
        else:
            print("Рейс не найден!")

    def get_flight(self, flight_id):
        return self.__flights.get(flight_id, None)

    def total_revenue(self):
        return sum(flight.get_revenue() for flight in self.__flights.values())

    def show_statistics(self):
        for flight_id, flight in self.__flights.items():
            info = flight.get_info()
            print(f"Рейс {flight_id}: {info}")


class Client:
    def __init__(self, name):
        self.name = name
        self.tickets = []

    def buy_ticket(self, airline, flight_id, ticket_type, quantity=1):
        flight = airline.get_flight(flight_id)
        if flight:
            flight.sell_ticket(ticket_type, quantity)
            self.tickets.append({"flight_id": flight_id, "type": ticket_type, "quantity": quantity})
        else:
            print("Рейс не найден!")

    def cancel_ticket(self, airline, flight_id, ticket_type, quantity=1):
        flight = airline.get_flight(flight_id)
        if flight:
            flight.cancel_ticket(ticket_type, quantity)
            
            for ticket in self.tickets:
                if ticket["flight_id"] == flight_id and ticket["type"] == ticket_type:
                    ticket["quantity"] -= quantity
                    if ticket["quantity"] <= 0:
                        self.tickets.remove(ticket)
                    break
        else:
            print("Рейс не найден!")

airline = Airline()
flight1 = Flight("Москва - Нью-Йорк", 100, 20, 500, 1500)
flight2 = Flight("Лондон - Париж", 50, 10, 200, 600)

airline.add_flight("F001", flight1)
airline.add_flight("F002", flight2)

client1 = Client("Алексей")
client1.buy_ticket(airline, "F001", "economy", 2)
client1.buy_ticket(airline, "F002", "business", 1)

airline.show_statistics()
print("Общая выручка:", airline.total_revenue())
