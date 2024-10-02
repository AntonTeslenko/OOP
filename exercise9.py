class ProductWithGetSet:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        self._price = price

class ProductWithProperty:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        self._price = price


class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, price):
        if price < 0:
            raise ValueError("Ціна не може бути від'ємною!")
        instance._price = price

class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name, price):
        self.name = name
        self.price = price

# Тест для ProductWithGetSet
product1 = ProductWithGetSet("Товар 1", 100)
print(f"{product1.name}: {product1.get_price()} злотих")
product1.set_price(150)
print(f"{product1.name} нова ціна: {product1.get_price()}злотих")


# Тест для ProductWithProperty
product2 = ProductWithProperty("Товар2", 200)
print(f"{product2.name}: {product2.price} злотих")
product2.price = 250
print(f"{product2.name} нова ціна: {product2.price}злотих")

# Тест для ProductWithProperty
product3 = ProductWithDescriptor("Товар3", 200)
print(f"{product3.name}: {product3.price} злотих")
product3.price = 150
print(f"{product3.name} нова ціна: {product3.price} злотих")

# Спроба встановити від'ємну ціну
try:
    product3.price = -50
except ValueError as e:
    print(e)

"""Використання геттерів і сеттерів - підхід, який найлегше зрозуміти,
   він дозволяє реалізувати перетворення даних прямо в методах. Метод з 
   використанням декораторів зменшує кількість рядків коду, дає можливість 
   зміни значення без зміни зовнішнього інтерфейсу. Дескриптори можна 
   використовувати в різних класах, що робить код бфльш повторно використовуваним, 
   але вони важкі для розуміння і вимагають більше рядків коду.
   Для більшості випадків декоратор @property є найбільш зручним через свою
   простоту і читабельність."""