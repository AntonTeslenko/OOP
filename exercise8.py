class Price:
    def __init__(self, sum):
        self.sum = round(sum, 2)

    def __add__(self, other):
        return Price(self.sum + other.sum)

    def __sub__(self, other):
        return Price(self.sum - other.sum)

    def __eq__(self, other):
        return self.sum == other.sum

    def __lt__(self, other):
        return self.sum < other.sum

    def __repr__(self):
        return f"Price: {self.sum:.2f}"

# Приклад використання програми

price1 = Price(10.837)
price2 = Price(4.8858)

# Додавання
price3 = price1 + price2
print("Cума: ", price3)

# Віднімання
price4 = price1 - price2
print("Різниця: ", price4)

# Порівняння
if price1 == price2:
    print("Ціни є однаковими")
elif price1 < price2:
    print("Ціна 1 менша за ціну 2")
else:
    print("Ціна 1 більша за ціну 2")

"""Клас Price міг би стати важливою частиною класу PaymentGateway, 
   а його операції додавання, віднімання та порівняння цін могли б
   бути використані для обчислення загальної вартості, виразування
   знижок, при цьому заокруглюючи значення до двох десяткових
   знаків, що могло б бути важливим фактором при обробці транзакцій"""