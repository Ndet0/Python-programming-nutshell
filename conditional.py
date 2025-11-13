marks=int(input("Enter your marks(e.g 74): "))

if marks >= 80:
    print("Grade: A")
elif marks >=70:
    print("Grade: B")
elif marks>=60:
    print("Grade: C")
elif marks>=50:
    print("Grade: D")
elif marks>=40:
    print("Grade: E")
else:
    print("Fail")


number = float(input("Enter number(e.g 2):"))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

username = input("Input username:")
password = input("Input password:")

if username == "TheJackal" and password == "Secret":
    print("Welcome back, Sir!")
else:
    print("Access denieed!")