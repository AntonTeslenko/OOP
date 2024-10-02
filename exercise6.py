class User:
    def __init__(self, first_name, last_name, email):
        self.verify_email(email)
        self._first_name = first_name
        self._last_name = last_name
        self._email = email

    @classmethod
    # Перевірка формату email адреси
    def verify_email(cls,email):

         if "@" in email and  "." in email:
             return email
         else:
             raise ValueError("email повинен містити символи '@' і '.' ")


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property

    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value


# Тестування програми

user = User("Джофрі", "Баратеон", "barateon@gmail.com")

print(user.first_name)
print(user.last_name)
print(user.email)


# Зміна значень за допомогою сеттерів

user.first_name = "Серсея"
user.last_name = "Ланістер"
user.email = "lanister@gmail.com"

print(user.first_name)
print(user.last_name)
print(user.email)
