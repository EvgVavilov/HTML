from decimal import Decimal

def task_01_money(rubles: int, coins: int, amount: int) -> Decimal:
    #rubles = Decimal(input("Введите кол-во рублей за единицу товара "))
    #coins = Decimal(input("Введите кол-во копеек за единицу товара "))
    #amount = Decimal(input("Введите кол-во товара "))
    task_01_money = (rubles + (coins/100))*amount
    return task_01_money


