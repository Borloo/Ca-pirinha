from typing import Self,Type

class BankAccount:
    def __init__(self, name: str = 'John', balance: float = 1000):
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        return self.display()

    def deposite(self, balance: float) -> bool:
        self.balance += balance
        print(f"[SUCCESS] New deposit : {self.display()}")
        return True

    def withdraw(self, balance: int) -> bool:
        if (self.balance - balance) < 0:
           print(f'[ERROR] You can\'t withdraw this amout : {self.display()}')
           return False
        
        self.balance -= balance
        print(f'[SUCCESS] New balance : {self.display()}')
        return True

    def display(self) -> str:
        return f'{self.name} - {round(self.balance, 2)}€'
    
    def send(self, other: Type[Self], balance: float) -> bool:
        if self.withdraw(balance):
            other.deposite(balance)
            return True
        
        print(f'[ERROR] You can\' send this amount {self.display()}')
        return False
        