# Создай класс BankAccount, который моделирует банковский счёт.
# Атрибуты приватные:
#  __owner — владелец счёта
#  __pin_code — пин-код (задаётся при создании)
#  __balance — баланс (по умолчанию 0)

# Методы:
#  1. get_balance(pin) — возвращает баланс, если пин-код правильный
#  2. deposit(dengi) — пополнение счёта (не требует пин-кода)
#  3. withdraw(dengi, pin) — снимает деньги, если хватает средств и пин-код правильный
#  4. change_pin(old_pin, new_pin) — смена пин-кода (проверяет старый пин)
#  5. info() — выводит имя владельца и “закрытый” баланс (например, "Баланс: **** сом")
class BankAccount:
    def __init__(self, owner, pin_code, balance):
        self.__owner = owner
        self.__pin_code = pin_code
        self.__balance = balance

    def get_balance(self, pin):
        if pin == self.__pin_code:
            return self.__balance
        else:
            print("Неверный пин-код")
            return None

    def deposit(self, dengi):
        self.__balance += dengi
        print(f"Счёт пополнен на {dengi} сом. Новый баланс: {self.__balance} сом")

    def withdraw(self, dengi, pin):
        if pin != self.__pin_code:
            print("Неверный пин-код")
            return False
        if dengi > self.__balance:
            print("Недостаточно средств")
            return False
        self.__balance -= dengi
        print(f"Снято {dengi} сом. Остаток: {self.__balance} сом")
        return True

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin_code:
            self.__pin_code = new_pin
            print("Пин-код успешно изменён")
            return True
        else:
            print("Неверный старый пин-код")
            return False

    def info(self):
        print(f"Владелец: {self.__owner}")
        print(f"Баланс: **** сом")  



account = BankAccount("Хадичабону", 1234, 5000)

account.info()
print("Баланс:", account.get_balance(1234))
account.deposit(1000)
account.withdraw(2000, 1234)
account.change_pin(1234, 4321)
account.withdraw(1000, 1234)  
account.withdraw(1000, 4321)  
