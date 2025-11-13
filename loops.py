# for i in range(5):
#     print("Bichanege!!")

# for num in range(1,6):
#     print("Number:", num)

# n = int(input("Enter a Number:"))

# for i in range(1, n + 1):
#     print ("counting:", i)


# fruits = ["apple","banana","mango"]

# for fruit in fruits:
#     print("I like", fruit)

# count = 1
# while count <=5:
#     print("loop number:", count)
#     count += 1

# while True:
#     print("This runs forever")

# for num in range(1,11):
#     print("numbers:",num)

# count = 5
# while count >= 1:
#     print("counting:", count)
#     count -= 1

# Ask the user to enter three names separated by commas
# names = input("Enter three names separated by commas: ")

# # Split the input string by commas to create a list of names
# names_list = names.split(",")

# # Loop through each name in the list
# for name in names_list:
#     # Remove extra spaces and print each name
#     print(name.strip())

# n = int(input("Enter a number:"))
# for i in range(1 ,n + 1):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# Initialize password as an empty string
password = ""

# Loop while the password is NOT "Secret"
# while password != "Secret":
#     # Ask the user to enter a password
#     password = input("Enter the password: ")
    
#     # If the entered password is wrong, show error message
#     if password != "Secret":
#         print("Access Denied! Try again.")

# # This line only runs after the loop exits (meaning correct password was entered)
# print("Access granted!")

# n = int(input("Enter a number :"))
# total = 0

# for i in range (1, n + 1):
#     total += i

# print("The total is:", total)


# names =[]

# while True:
#     name = input("Enter a name (or type stop to finish):")

#     if name.lower() == "stop":
#        break
#     names.append(name)

#     print("You entered the following names:")
#     for n in names:
#         print("-",n)


# num = int(input("Enter a number:"))

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")


# for i in range (1,6):
#     if i == 3:
#         continue
#     print(i)


# for i in range (1,11):
#     if i == 8:
#         break
#     print(i)

# limit = int(input("Enter  number:"))

# count = 1
# while count <= limit:
#     print("Count:", count)
#     count += 1

# password ="python123"
# guess = ""

# while guess != password:
#     guess = input("Enter your passsword:")
#     if guess != password:
#         print("Access Denied! Try again")
#     elif guess == password:
#         print("Access Granted!")
#     else:
#         print("Unexpected error occurred.")

# import random

# secret = random.randint(1,10)
# guess = 0

# while guess !=secret:
#     guess = int(input("Guess the number between 1 and 10:"))
#     if guess < secret:
#         print("Too low! Try again.")
#     elif guess > secret:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")


# num = int(input("Enter a number to create multiplication table:"))

# for i in range (1,12):
#     print(f"{num} x {i} = {num * i }")

import time

start = int(input("Enter number to start countdown:"))

while start >=0:
    print(start)
    time.sleep(1)
    start -=1

for i in range(5):
     print("Bichanege!!")