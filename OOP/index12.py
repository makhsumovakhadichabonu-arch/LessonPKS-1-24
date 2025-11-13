class BankAccount:
    def __init__(self, owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount): # пополнение счета
        if amount <= 0:
            print("Сумма должно быть положительной")
            return
        self.balance += amount
        print(f"{self.owner} пополнил счет на {amount} сом, теперь у вас {self.balance}сом")
        
    def withdraw(self,amount): # снятие со счета
         if amount > self.balance:
             print("Недостаточно средств")
             return
         if amount <= 0:
             print("Сумма должно быть положительной")
             return
         self.balance -= amount
         print(f"{self.owner} снял счет на {amount} сом, теперь у вас {self.balance}сом")
    
    def info(self):
        return f"Владелец: {self.owner} Ваш баланс: {self.balance} сом"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_accounts(self,owner):# создает новый счет
        account = BankAccount(owner)
        self.accounts.append(account)
        print(f"Открыт новый счет для {owner} в банке. {self.name}")
        return account
    
    def find_account(self,owner): # возвращает счет по имени
        for acc in self.accounts:
            if acc.owner == owner:
                 print(f" {owner} Зарегистрован в банке")
                 return acc
        print(f"не найден{owner} ")
        return None
        
    def transfer(self, from_owner, to_owner, amount): # перевод денег между счетами
      from_acc =self.find_account(from_owner)
      to_acc = self.find_account(to_owner)
      if not from_acc or not to_acc:
          print("Перевод невозможен")
          return
      if from_acc.balance < amount:
          print("Недостаточно средств")
          return
      from_acc.withdraw(amount)
      to_acc.deposit(amount)
      print(f"Перевод {amount} сом от {from_owner} к {to_owner} выполнен")
        
bank = Bank("ПКС Банк")
acc1 = bank.open_accounts('Шодияна')
acc2 = bank.open_accounts('Абай')
acc1.deposit(3000)
acc2.deposit(19000)
acc1.info()
acc2.info()
bank.transfer('Абай', 'Шодияна', 3200)
acc1.info()
acc2.info()
