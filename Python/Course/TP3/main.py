from point_2d import *
from bank_account import *
from savings_account import *

def main_point_2d():
    point_a = Point2D(3 ,5)
    point_b = Point2D(3, 10)
    print(point_a.distance_to_origin())
    print(point_b.distance_to_origin())
    print(point_a.distance_to_other(point_b))
    print(point_b.distance_to_other(point_a))

def main_bank_account():
    bank_account_borloo = SavingsAccount('Borloo', 5)
    bank_account_tutouan = SavingsAccount('Tutouan', 10000)

    # bank_account_borloo.display()
    # bank_account_borloo.deposite(10)
    # bank_account_borloo.withdraw(5)
    # bank_account_borloo.withdraw(20)

    bank_account_borloo.send(bank_account_tutouan, 100)
    bank_account_tutouan.send(bank_account_borloo, 100)

    bank_account_borloo.capitalization(12)
    bank_account_tutouan.capitalization(12)

    print(bank_account_borloo)
    print(bank_account_tutouan)

# main_point_2d()
main_bank_account()