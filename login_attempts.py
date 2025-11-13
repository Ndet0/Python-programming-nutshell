username = "TheJackal"
password = "Secret"

attempts = 0

while attempts < 3:
    input_username = input("Input username:")
    input_password = input("Input password:")

    if input_username == username and input_password == password:
        print("Access Granted!")
        break
    else:
        print("Access Denied! Try again.")
        attempts += 1
        print(f"You have {3 - attempts} attempts left.")

if attempts == 3:
    print("Too many failed attempts. Access denied.")
