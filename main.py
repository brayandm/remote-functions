from client import run
import random


class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def get_info(self):
        return f"Amount: {self.amount}"


class Person:
    def __init__(self, name, age, wallet: Wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age} with {self.wallet.get_info()}"


@run("localhost")
def hello(me: Person):
    return f"Hello, {me.get_info()}"


@run("localhost")
def random_guess():

    maxi = 1000000

    hide = random.randint(1, maxi)

    while random.randint(1, maxi) != hide:
        continue

    return hide


me = Person("John", 30, Wallet(101))

print(hello(me))

print(random_guess())
