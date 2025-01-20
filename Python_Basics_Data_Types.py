# Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.
# a= 1
# b=1.0
# c="1"
# print("value of a :",a, "type:",type(a))
# print("value of b :",b, "type:",type(b))
# print("value of c :",c, "type:",type(c))

#Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.
# a=2
# print("a as an integer",type(a))
# a=2.0
# print("a as a float",type(a))
# a='2'
# print("a as a str",type(a))

#. Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c..
# a=b=c=10
# print("value of a:", a, "value of b:",b,"value of c:",c )

# Assign two variables a and b as integer and print the sum of a+b.
# a=2
# b=3
# print("sum of a & b",a+b)


# Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
# a=["apple", "banana", "cherry", "date", "elderberry"]"
# print(a,type(a))



# How do you access the second and fourth elements from the list.
# print("2nd element of list:", a[1], "& 4th element of the list:",a[3])

#Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.
# num=[10, 20, 30, 40, 50]
# num[2]=35
# print(num)


# Create a Tuple:How do you create a tuple with the following elements: "red", "green", "blue"?
# a=("red", "green", "blue")
# print(a,type(a))

# Access Elements in a Tuple:How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
# colors = ("red", "green", "blue", "yellow")
# print(colors[0],colors[3])

# Immutable Nature of Tuples:What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
# colors = ("red", "green", "blue")
# colors[1]="yellow"
# print(colors)


# Tuple Unpacking:Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
# coordinates = (10, 20, 30)
# a=coordinates[0]
# b=coordinates[1]
# c=coordinates[2]
# print(a,b,c)



# Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
# colors = ("red", "green", "blue")
# if "blue" in colors:
#     print("yes")
# else:
#     print("no")

# Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print("length of the tuple:",len(days))


# Create a Dictionary:Create a dictionary where the keys are student names and the values are their grades. For example:
# python
# {"Alice": 85, "Bob": 90, "Charlie": 78}

# a={"Alice": 85, "Bob": 90, "Charlie": 78}


# How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# grade=students["Bob"]
# print(grade)


# Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# del students["Charlie"]
# students["David"]=92
# print(students)


# Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# students["Bob"]=95
# print(students)


# Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# if "Alice" in students:
#     print("yes")
# else:
#     print("no")

# Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.
# students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# for key,values in students.items():
#     print(f"key:{key},value:{values}")



