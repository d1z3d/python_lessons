import math
import sys
from typing import Tuple, List
sys.stdout.reconfigure(encoding='utf-8')

class Turtle:
    def __init__(self, x: int = 0, y: int = 0, s: int = 1):
        if s <= 0:
            raise ValueError("Шаг должен быть положительным")
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("Нельзя уменьшить шаг ниже 1")
        self.s -= 1

    @staticmethod
    def _divisors(n: int) -> List[int]:
        n = abs(n)
        if n == 0:
            return []
        divs = set()
        for i in range(1, int(math.isqrt(n)) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
        return sorted(divs)

    def count_moves(self, x2: int, y2: int) -> int:
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        if dx == 0 and dy == 0:
            return 0

        g = math.gcd(dx, dy)
        candidates = self._divisors(g)


        best = None
        for k in candidates:
            moves = dx // k + dy // k
            adjust = abs(self.s - k)
            total = moves + adjust
            if best is None or total < best:
                best = total
        return best
