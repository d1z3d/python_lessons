import sys
sys.stdout.reconfigure(encoding='utf-8')

class Kassa:
    def __init__(self, initial_amount: int = 0):
        self.balance = initial_amount

    def top_up(self, amount: int):
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной")
        self.balance += amount

    def count_1000(self) -> int:
        return self.balance // 1000

    def take_away(self, amount: int):
        if amount < 0:
            raise ValueError("Сумма изъятия не может быть отрицательной")
        if self.balance < amount:
            raise ValueError("Недостаточно денег в кассе")
        self.balance -= amount
