# # Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
# a=int(input("enter 1st no."))
# b=int(input("enter 2nd no."))
# # sum:
# print(a+b)
# # subtraction:
# print(a-b)
# # multiplication:
# print(a*b)
# # division:
# print(a/b)
# # modulus:
# print(a%b)



# # Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
# a=int(input("enter 1st no."))
#
# if (a%2)==0:
#     print("even")
# else:
#     print("odd")


# # Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
# a=int(input("enter 1st no."))
# if (a>0):
#     print("positive")
# elif (a<0):
#     print("negative")
# else:
#     print("zero")

# Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
#
# 90 and above: A
# 80 - 89: B
# 70 - 79: C
# 60 - 69: D
# Below 60: F
#
# a=int(input("enter the marks"))
# if (a>=90):
#     print("A")
# elif (79<a<90):
#     print("B")
# elif (69<a<80):
#     print("C")
# elif (59<a<70):
#     print("D")
# else:
#     print("F")

# # # Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
# with open("sample.txt","w") as file:
#     file.write(str(input("write something")))
# with open("sample.txt","r") as file:
#     text=file.read()
# #     print(text)
#
# # Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
# word_count=len(text.split())
# print(word_count)

# # Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.
# for n in range(1,11):
#     print(n)

# # Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.
# a=int(input("enter the number"))
# for n in range (1,11):
#     b=a*n
#     print(a,"x",n,"=",b)
