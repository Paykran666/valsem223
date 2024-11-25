class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостаточно средств или сумма снятия некорректна.")


account = BankAccount("12345678", 1000)
print(f"Начальный баланс: {account.get_balance()}")
account.deposit(500)
account.withdraw(200)
print(f"Текущий баланс: {account.get_balance()}") # Текущий баланс
account.withdraw(2000) #Проверка на недостаток средств
