class Price:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"({self.amount}, {self.currency})"

    def __add__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount + other.amount), currency=self.currency)
        return instance

    def __sub__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount - other.amount), currency=self.currency)
        return instance

    def __mul__(self, other: "Price") -> "Price":
        instance = Price(amount=(self.amount * other.amount), currency=self.currency)
        return instance


price_a = Price(20000, "UAH")
price_b = Price(30000, "UAH")

total = price_a + price_b
print(str(total))

total = price_a - price_b
print(str(total))

total = price_a * price_b
print(str(total))
