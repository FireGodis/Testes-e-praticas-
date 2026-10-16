from dataclasses import dataclass
from typing import Protocol

class Discount(Protocol):
    def apply(self, amount: float) -> float: ...

@dataclass(frozen=True)
class PercentageDiscount:
    rate: float
    def apply(self, amount: float) -> float:
        if amount < 0 or not 0 <= self.rate <= 1:
            raise ValueError("Valor ou taxa inválidos")
        return amount * (1 - self.rate)

def final_price(amount: float, discount: Discount) -> float:
    return discount.apply(amount)

if __name__ == "__main__":
    print(final_price(100.0, PercentageDiscount(rate=0.10)))
