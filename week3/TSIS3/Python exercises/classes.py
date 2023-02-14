class InputOutputString:
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string: ")

    def print_string(self):
        print(self.s.upper())
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, other_point):
        delta_x = other_point.x - self.x
        delta_y = other_point.y - self.y
        return math.sqrt(delta_x**2 + delta_y**2)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Current balance: {self.balance}")

acct = Account("Dias Kuspanov", 650)

acct.deposit(300)
acct.deposit(7)

acct.withdraw(600)
acct.withdraw(400)
