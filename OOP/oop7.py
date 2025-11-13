# «Симуляция банка» — создать объектную модель банка, где клиенты могут:
# открывать депозиты, брать кредиты, оформлять рассрочки на товары.
# Банк должен уметь учитывать эти операции и подсчитывать свою прибыль.

# 1.класс Person
# Атрибуты: name, age, balance
# Методы: deposit(amount) — пополнение счёта.
# withdraw(amount) — снятие со счёта.
# info() — возвращает краткую информацию о клиенте.

# 2.класс Bank
# Атрибуты: name, clients — список объектов Person
# products — список активных продуктов (депозиты, кредиты, рассрочки), income — доход банка
# Методы: add_client(client), add_product(product)
# calculate_total_profit() — суммирует доходы по всем продуктам.

# 3. класс BankProduct (базовый класс)
# Атрибуты: client, amount, interest_rate, term_months
# Методы: calculate_interest() — рассчитывает сумму процентов.
# info() — краткая информация о продукте.

# 4.класс Deposit (наследник BankProduct)
# Деньги клиента передаются банку, и по окончании срока клиент получает сумму + проценты.
# Метод close_deposit() возвращает клиенту деньги и начисленные проценты.

# 5.класс Credit (наследник BankProduct)
# Банк выдаёт клиенту деньги, которые тот должен вернуть с процентами.
# Метод monthly_payment() рассчитывает ежемесячный платёж по кредиту.
# Метод close_credit() возвращает банку тело кредита и проценты (уменьшает баланс клиента).

# 6. класс Installment (Рассрочка)
# Клиент покупает товар в рассрочку (без процентов, но с комиссией).
# Атрибуты: product_name, commission_rate
# Методы: monthly_payment(), close_installment()

class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} пополнил счет на {amount} ") 

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} снятие счет на {amount} ")
        else:
            print(f'Недостаточно средств, у вас только {self.balance}')

    def info(self):
        print(f"{self.name}, возраст: {self.age}, баланс: {self.balance} сом.")


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.products = []
        self.income = 0

    def add_client(self, client):
        self.clients.append(client)
        print(f'Клиент {client.name} добавлен')

    def add_product(self, product):
        self.products.append(product)
        print(f'Продукт добавлен')

    def add_income(self, amount):
        self.income += amount

    def calculate_total_profit(self):
        return self.income

    def show_clients(self):
        print("Наши клиенты:")
        for c in self.clients:
            c.info()


class BankProduct:
    def __init__(self, client, amount, interest_rate, term_months):
        self.client = client
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_months = term_months

    def calculate_interest(self):
        return self.amount * (self.interest_rate / 100) * (self.term_months / 12)

    def info(self):
        print(f"{self.client.name}, сумма: {self.amount} сом, ставка: {self.interest_rate}%, срок: {self.term_months} мес.")

class Deposit(BankProduct):
    def close_deposit(self):
        interest = self.calculate_interest()
        total = self.amount + interest
        self.client.balance += total
        print(f"{self.client.name}, ваш депозит закрыт.")
        print(f"Основная сумма: {self.amount}")
        print(f"Начисленные проценты: {interest:.2f}")
        print(f"Итого возвращено: {total:.2f}")

class Credit(BankProduct):
    def monthly_payment(self):
        monthly_rate = self.interest_rate / 100 / 12
        payment = self.amount * (monthly_rate * (1 + monthly_rate) ** self.term_months) / ((1 + monthly_rate) ** self.term_months - 1)
        return payment

    def close_credit(self):
        total_payment = self.monthly_payment() * self.term_months
        self.client.balance -= total_payment
        print(f"{self.client.name}, ваш кредит закрыт.")
        print(f"Сумма кредита: {self.amount}")
        print(f"Всего выплачено (с процентами): {total_payment:.2f}")
        print(f"Оставшийся баланс клиента: {self.client.balance:.2f}")

class Installment(BankProduct):
    def __init__(self, client, product_name, product_price, months, commission_rate):
        super().__init__(client, product_price, 0, months)
        self.product_name = product_name
        self.commission_rate = commission_rate

    def monthly_payment(self):
        commission = self.amount * (self.commission_rate / 100)
        total = self.amount + commission
        monthly = total / self.term_months
        return monthly

    def close_installment(self):
        total_payment = self.monthly_payment() * self.term_months
        self.client.balance -= total_payment
        print(f"{self.client.name}, рассрочка по товару '{self.product_name}' закрыта.")
        print(f"Цена товара: {self.amount}")
        print(f"Комиссия: {self.commission_rate}%")
        print(f"Итого выплачено: {total_payment:.2f}")
        print(f"Оставшийся баланс клиента: {self.client.balance:.2f}")


bank = Bank("Harvard Bank")
client1 = Person("Хадичабону", 16, 20000)

bank.add_client(client1)

print("\nДЕПОЗИТ")
deposit = Deposit(client1, 10000, 10, 6)
deposit.close_deposit()

print("\nКРЕДИТ")
credit = Credit(client1, 5000, 12, 12)
credit.close_credit()

print("\nРАССРОЧКА")
installment = Installment(client1, "Ноутбук", 12000, 6, 5)
installment.close_installment()

print("\nФинальный баланс клиента:")
client1.info()
