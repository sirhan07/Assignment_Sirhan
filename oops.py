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

class animal():
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(Self):
        print("bark")
Animal = animal()
Animal.sound() 

Dog = dog()
Dog.sound()