from bank_account import *
from typing import Self, Type

class SavingsAccount(BankAccount):
    def __init__(self, name: str = 'John', balance: int = 1000, monthly_interest: float = 0.3):
        super().__init__(name, balance)
        self.monthly_interest = monthly_interest

    def __str__(self):
        return f'{self.display()}, Monthly Interest : {self.monthly_interest}'

    def set_rate(self, monthly_interest: float):
        self.monthly_interest = monthly_interest

    def capitalization(self, month_count: int) -> None:
        self.balance *= (1 + self.monthly_interest) ** month_count