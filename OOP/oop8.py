# Задача Симуляция компьютерного клуба
# создаём систему для комп клуба, где можно бронировать и оплачивать места.
# Каждый компьютер имеет свою цену за час, статус (свободен/занят), и время, когда его забронировали.
# Клиенты могут садиться за компьютер, играть и оплачивать время.
# Владелец клуба может смотреть выручку и управлять компьютерами.

# 1. класс Computer
# Инкапсулированный класс, представляющий компьютер.
# Атрибуты:
# __id — уникальный номер (инкапсулированный, доступ через свойство).
# __hourly_rate — цена за час (инкапсулированный, управляется через @property).
# _is_busy — защищённый атрибут (True/False).
# _current_client — текущий клиент или None.
# _start_time — время начала сессии.
# Методы:
# start_session(client, hours) — запускает сессию, делает компьютер занятым.
# end_session() — завершает сессию, считает оплату.
# info() — краткое состояние компьютера.
# Свойства:
# hourly_rate — с @property и @setter: цена не может быть ниже 50 сом.
# id — только для чтения (@property, без setter).

# 2. Client
# Атрибуты: name, balance
# Методы:
# pay(amount) — уменьшает баланс, если хватает денег.
# add_balance(amount) — пополнение счёта.
# info() — информация о клиенте.

# 3. Club
# Атрибуты: name, computers — список объектов Computer
# _income — защищённый атрибут, выручка клуба.
# Методы:
# add_computer(computer)
# find_free_computer()
# serve_client(client, hours) — находит свободный комп, запускает сессию.
# end_all_sessions() — завершает все активные сессии и увеличивает доход клуба.
# show_status() — показывает состояние всех компьютеров и доход.

class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id              
        self.__hourly_rate = hourly_rate  
        self._is_busy = False             
        self._current_client = None       
        self._start_time = 0              

    @property
    def id(self):
        return self.__id

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate <= 50 and new_rate <=1000:   
            self.__hourly_rate = new_rate

    def start_session(self, client, hours):
        if self._is_busy:
            print("занят комп")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True
            self._current_client = client
            self._start_time = hours
            print(f"Клиент {client.name} сел за компьютер {self.__id} на {hours}час, на{cost}сом.")

    def end_session(self, end_time):
        if not self._is_busy:
            print(f" Компьютер {self.__id} не используется.")
            return 0
        self._is_busy = False
        income = self.__hourly_rate*self._start_time
        client_name = self._current_client = None
        self._start_time = 0
        return income

    def info(self):
        status = "Занят" if self._is_busy else "Свободен"
        return f"Комп {self.id} {status} { self.__hourly_rate
}сом/ч"


class  Client:
    def __init__(self,  name, balance):
        self.name = name
        self.balance = balance
        

    def pay(self, amount):
          if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} оплатил {amount} сом. Остаток: {self.balance} сом.")
            return True
          else:
            print(f"У {self.name} недостаточно денег! Оплата не выполнена.")
            return False


    def  add_balance(self, amount):
        self.balance += amount
        print(f"Баланс {self.name} пополнен на {amount} сом. Новый баланс: {self.balance} сом.")

    def info(self):
         print(f"Клиент: {self.name}, Баланс: {self.balance} сом")


class Club:
    def __init__(self, name):
        self.name = name                
        self.computers = []            
        self._income = 0                

    def add_computer(self, computer):
        self.computers.append(computer)
        print(f"Компьютер {computer.id} добавлен в клуб {self.name}.")

    def find_free_computer(self):
        for comp in self.computers:
            if not comp._is_busy:
                return comp
        return None

    def serve_client(self, client, hours):
        comp = self.find_free_computer()
        if comp:
            comp.start_session(client, hours)
        else:
            print("Все компьютеры заняты!")

    def end_all_sessions(self, end_time):
        for comp in self.computers:
            if comp._is_busy:
                income = comp.end_session(end_time)
                self._income += income

    def show_status(self):
        print(f"Клуб {self.name} — выручка: {self._income} сом")
        for comp in self.computers:
            print(comp.info())
@property
def income(self):
    return self._income

cyber_club = Club("CyberZone")

comp1 = Computer(1, 100)
comp2 = Computer(2, 150)
comp3 = Computer(3, 200)

cyber_club.add_computer(comp1)
cyber_club.add_computer(comp2)
cyber_club.add_computer(comp3)

ali = Client("Али", 500)
beka = Client("Бека", 200)
dina = Client("Дина", 800)

ali.info()
beka.info()
dina.info()

print("\nКлиенты садятся за компьютеры ")
cyber_club.serve_client(ali, 3)   
cyber_club.serve_client(beka, 2)  
cyber_club.serve_client(dina, 4)  

print("\nСостояние компьютеров после старта сессий")
cyber_club.show_status()

print("\nЗавершаем все сессии через 5 часов ")
cyber_club.end_all_sessions(5)

print("\nСостояние компьютеров после окончания сессий ")
cyber_club.show_status()

print("\n Баланс клиентов после сессий")
ali.info()
beka.info()
dina.info()
