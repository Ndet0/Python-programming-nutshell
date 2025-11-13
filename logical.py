is_member = input("Are you a member? (yes/no):")
spent = float(input("How much did you spend?"))

if is_member == "yes" or spent > 1000:
    print("You get a discount!")
else:
    print("No discount, sorry")

is_logged_in = True 
is_admin = False 

print(is_logged_in and is_admin)
print(is_logged_in or is_admin)
