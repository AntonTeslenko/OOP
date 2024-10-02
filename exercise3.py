class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __repr__(self):
        return f"{self.name}: {self.age}"


people = [Person("Брюс Уілліс", 43),
          Person("Міла Йовович", 29),
          Person("Гаррі Олдман", 47)
          ]


# Сортування списку за віком
for i in range(len(people)):
    for j in range(i + 1, len(people)):
        if people[j] < people[i]:
            people[i], people[j] = people[j], people[i]


print(people)
