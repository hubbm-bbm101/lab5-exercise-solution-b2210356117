# Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot (disregard the order for
# the sake of simplicity). Use that function to check if a user input is a valid e-mail or not.

email = input("enter your mail: ")

symbol_1 = False
symbol_2 = False

for i in email:
    if i == "@":
        symbol_1 = True
    elif i == ".":
        symbol_2 = True

if symbol_1 and symbol_2:
    print("This is a valid e-mail address.")
else:
    print("This isn't a valid e-mail address")