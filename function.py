# def function_name():
#  print("hello world")

# function_name()

# def greet(name= "friend"):
#     print(f"Hello, {name}")

# greet()
# greet("Jacakl")

# def add(a, b):
#  return a + b

# result = add (5,5)
# print("Sum is:", result)

#Grading system
# def get_grade(marks):
#   if marks >=80:
#    return "A"
#   elif marks >=60:
#     return "B"
#   elif marks >=40:
#         return "C"
#   else:
#         return "F"
  
# marks = int(input("Enter your marks:"))
# print("Your grade is:", get_grade(marks))

# def countdown(n):
#   while n > 0:
#      print("counting:", n)
#      n -= 1
#   print("Blastoff!")

# n = int(input("Enter a number to countdown from: "))
# countdown(n)

# def square(n):
#  result = n**2
#  print(f"The square of {n} is {result}")

# n = int(input("Enter number:"))
# square(n) 


# def greet_age(name="friend", age= None):
#     print(f"Hello {name}, you are {age} years old!")

# name = input("Enter your name:")
# age = input("Enter your age:")
# greet_age(name,age)

# greet_age("festus",20)

# def check_number(n):
#     if n % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")

# n = int(input("Enter number:"))
# check_number(n)


# def check_largest(num1,num2,num3):
    # largest= num1
    # if num2 > largest:
    #     largest = num2
    # if num3 > largest:
    #     largest = num3
    # print(f"The largest number is {max((num1,num2,num3))}")

# check_largest(6,7,8)


# def password_strength(password: str) -> str:
#     """Return 'strong' if password length >= 8, otherwise 'weak'.

#     Note: user query spelled 'storng' — assuming this was a typo and
#     returning the standard spelling 'strong'. If you need the exact
#     misspelling, tell me and I'll change it.
#     """
#     return "strong" if len(password) >= 8 else "weak"

# password = input("Enter password to check strength:")
# password_strength()
# Quick manual tests
# if __name__ == "__main__":
#     samples = ["pass123", "password", "hunter2", "longpassword123"]
#     for s in samples:
#         print(f"{s!r}: {password_strength(s)}")
#   while n > 0:
#      print("counting:", n)
#      n -= 1
#   print("Blastoff!")

# n = int(input("Enter a number to countdown from: "))
# countdown(n)

# def square(n):
#  result = n**2
#  print(f"The square of {n} is {result}")

# n = int(input("Enter number:"))
# square(n) 


# def greet_age(name="friend", age= None):
#     print(f"Hello {name}, you are {age} years old!")

# name = input("Enter your name:")
# age = input("Enter your age:")
# greet_age(name,age)

# greet_age("festus",20)

# def check_number(n):
#     if n % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")

# n = int(input("Enter number:"))
# check_number(n)


# def check_largest(num1,num2,num3):
    # largest= num1
    # if num2 > largest:
    #     largest = num2
    # if num3 > largest:
    #     largest = num3
    # print(f"The largest number is {max((num1,num2,num3


#!/usr/bin/env python3

def greet_programmer():
    pass
print("hello, programmer!")

def greet(name):
    pass
    print(f"hello, {name}!")




def greet_with_default(name="Bichange"):
    pass
    print(f"hello, {name}!")



def add(num1, num2):
    pass
    print(f"Thes sum is : {num1 + num2}")

def halve(number):
    pass
    if isinstance(number, int) or isinstance(number, float):
        print(number / 2)

number = int(input("Enter a number to halve: "))


greet_programmer()
greet("Jackal")
greet_with_default()
add(3, 5)
halve(number)