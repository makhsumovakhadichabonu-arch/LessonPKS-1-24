# Делаем с помощью ООП используя классы и всё что проходили
# Фитнес-клуб “Iron Body PRO”
# Создай программу для фитнес-клуба “Iron Body PRO”, где пользователи могут регистрироваться, входить, управлять балансом и абонементами(тариф), а также — получать бонусы за активность.
# Когда клиент заходит, программа спрашивает:
# “Вы уже зарегистрированы в Iron Body PRO? (да/нет)”
# Если ответ "нет":
# Клиент проходит регистрацию:
# вводит логин, пароль, возраст, номер телефона;
# получает бонус 300 сом на счёт при регистрации;
# данные сохраняются в clients.
# Если ответ "да":
# Программа проверяет наличие клиента в базе:
# если найден, запрашивает пароль (3 попытки);
# если пароль верный — вход успешен;
# если 3 раза неправильно — аккаунт временно заблокирован;
# если логина нет — программа отправляет на регистрацию.
# print("""
# 1. Проверить баланс
# 2. Пополнить баланс
# 3. Купить абонемент
# 4. Посмотреть историю покупок
# 5. Перевести деньги другому пользователю
# 6. Получить бонус за посещения
# 7. Выйти""")
# tariffs = {
# "1 день": 150,
# "1 неделя": 800,
# "1 месяц": 2500,
# "3 месяца": 6000,
# "VIP-год": 15000
# }
# Если денег хватает, стоимость списывается с баланса.
# После покупки абонемента:
# Добавляется запись в history.
# Клиент получает +5% бонуса от стоимости на счёт (“Кэшбэк здоровья”).
clients = {
"Алмаз Эшимбеков": {
"password": "12345",
"balance": 2500,
"age": 25,
"phone": "+996700123456",
"history": ["1 неделя", "1 месяц"],
"visits": 3,
"is_blocked": False
}
}
tariffs = {
    "1 день": 150,
    "1 неделя": 800,
    "1 месяц": 2500,
    "3 месяца": 6000,
    "VIP-год": 15000
}

class Client:
    def __init__(self, name, password, age, phone):
        self.name = name
        self.password = password
        self.age = age
        self.phone = phone
        self.balance = 300  # бонус при регистрации
        self.history = []
        self.visits = 0
        self.is_blocked = False

    def check_balance(self):
        print(f"Баланс: {self.balance} сом")

    def add_balance(self, amount):
        self.balance += amount
        print(f"Баланс пополнен на {amount} сом. Новый баланс: {self.balance} сом")

    def buy_tariff(self, tariff_name):
        if tariff_name in tariffs:
            price = tariffs[tariff_name]
            if self.balance >= price:
                self.balance -= price
                self.history.append(tariff_name)
                bonus = price * 0.05
                self.balance += bonus
                print(f"Вы купили '{tariff_name}'. Кэшбэк: {int(bonus)} сом. Баланс: {int(self.balance)} сом")
            else:
                print("Недостаточно средств для покупки")
        else:
            print("Такого тарифа нет")

    def show_history(self):
        if self.history:
            print("История покупок:", ", ".join(self.history))
        else:
            print("История покупок пустая")

    def add_visit_bonus(self):
        bonus = 50
        self.balance += bonus
        self.visits += 1
        print(f"Бонус за посещение: {bonus} сом. Баланс: {self.balance} сом")

    def transfer_money(self, other_client, amount):
        if self.balance >= amount:
            self.balance -= amount
            other_client.balance += amount
            print(f"Переведено {amount} сом пользователю {other_client.name}")
        else:
            print("Недостаточно средств для перевода")


clients = {
    "Алмаз Эшимбеков": Client("Алмаз Эшимбеков", "12345", 25, "+996700123456")
}

while True:
    registered = input("Вы уже зарегистрированы в Iron Body PRO? (да/нет): ").lower()

    if registered == "нет":
        name = input("Введите ваше имя: ")
        password = input("Введите пароль: ")
        age = int(input("Введите возраст: "))
        phone = input("Введите номер телефона: ")
        client = Client(name, password, age, phone)
        clients[name] = client
        print(f"Регистрация успешна! Вам начислено 300 сом бонуса.")
        current_client = client
        break

    elif registered == "да":
        name = input("Введите логин: ")
        if name in clients:
            attempts = 0
            while attempts < 3:
                password = input("Введите пароль: ")
                if password == clients[name].password:
                    print("Вход успешен! Добро пожаловать в Iron Body PRO")
                    current_client = clients[name]
                    break
                else:
                    attempts += 1
                    print(f"Неверный пароль. Попытка {attempts}/3")
            else:
                clients[name].is_blocked = True
                print("Аккаунт временно заблокирован")
                continue
            break
        else:
            print("Пользователь не найден. Нужно зарегистрироваться.")
    else:
        print("Ответьте 'да' или 'нет'.")

while True:
    print("""
1. Проверить баланс
2. Пополнить баланс
3. Купить абонемент
4. Посмотреть историю покупок
5. Перевести деньги другому пользователю
6. Получить бонус за посещения
7. Выйти
""")
    choice = input("Выберите действие: ")

    if choice == "1":
        current_client.check_balance()
    elif choice == "2":
        amount = int(input("Сколько хотите пополнить?: "))
        current_client.add_balance(amount)
    elif choice == "3":
        print("Доступные тарифы:")
        for t, price in tariffs.items():
            print(f"{t} - {price} сом")
        tariff_name = input("Введите название тарифа: ")
        current_client.buy_tariff(tariff_name)
    elif choice == "4":
        current_client.show_history()
    elif choice == "5":
        target_name = input("Введите логин получателя: ")
        if target_name in clients:
            amount = int(input("Сумма перевода: "))
            current_client.transfer_money(clients[target_name], amount)
        else:
            print("Пользователь не найден")
    elif choice == "6":
        current_client.add_visit_bonus()
    elif choice == "7":
        print("Выход. До свидания!")
        break
    else:
        print("Неверный выбор.")
