# Assignment 1: Static Methods
# Create a class MathOperations that contains:
# A static method add_numbers that takes two arguments and returns their sum.
# A static method multiply_numbers that takes two arguments and returns their product.


# class sum:
#     def add(a,b):
#         c=a + b  
#         return c

#     def multiply(a,b):
#         c=a*b
#         return c
# x=10
# y=20
# print("sum", sum.add(x,y))
# print("product",sum.multiply(x,y))

# Assignment 2: Class Methods
# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.


# class Person:
  
#     count = 0

#     def __init__(self):
       
#         Person.count += 1

#     @classmethod
#     def people(cls):
#         # Return the current count of instances
#         return cls.count
# person1 = Person()
# person2 = Person()
# person3 = Person()


# print( Person.people())

# Assignment 3: Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.
# class temp():
#     def convert(a):
#          return (a* 9/5) + 32
#     def statement():
#         return("coverted from celcius to fahrenheit")
# b=30
# print(temp.convert(b))
# print(temp.statement())

# class animal():
#     def sound(self):
#         print("animal sound")
# class dog(animal):
#     def sound(Self):
#         print("bark")
# Animal = animal()
# Animal.sound() 

# Dog = dog()
# Dog.sound()
# Assignment 5: Multiple Inheritance
# class Bird:
#     def fly(self):
#         print("Flying")


# class Fish:
#     def swim(self):
#         print("Swimming")

# class Duck(Bird, Fish):
#     pass


# duck = Duck()


# duck.fly()  
# duck.swim()  

# Assignment 7: Encapsulation
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited ${amount}. Current balance: ${self._balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrew ${amount}. Current balance: ${self._balance}")
#             else:
#                 print("Insufficient balance.")
#         else:
#             print("Withdrawal amount must be positive.")

#     def get_balance(self):
#         return self._balance


# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# print("Final balance:", account.get_balance())

# Assignmemnt 8 :
# class Dog:
#     def speak(self):
#         print("Woof")

# class Cat:
#     def speak(self):
#         print("Meow")

# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()


# Assignment 9
# class Calculator:
#     def add(self, num1, num2, num3=0):
#         return num1 + num2 + num3

# calc = Calculator()

# result1 = calc.add(5, 10)
# print("Sum of two numbers:", result1)

# result2 = calc.add(5, 10, 15)
# print("Sum of three numbers:", result2)
