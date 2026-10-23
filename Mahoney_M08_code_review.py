'''
    script: Mahoney_M08_code_review_UPDATED.py
    action: corrects errors in object and class code examples
    author: Erin Mahoney
    date:   07/20/2026
'''

# Problem 1
class Car:
    def __init__(self, make, model, year):
        # Fixed: Added self as the first parameter so the object can store attributes.
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Camry", 2022)
print(car1.display_info())


# Problem 2
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        # Fixed: Added self and updated self.balance instead of a local variable.
        self.balance = self.balance + amount


account = BankAccount(1000)
account.deposit(500)
print(account.balance)


# Problem 3
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name, breed):
        # Fixed: Called the parent class constructor so name is initialized.
        super().__init__(name)
        self.breed = breed


dog = Dog("Buddy", "Golden Retriever")
print(dog.name)
print(dog.breed)
print(dog.speak())
