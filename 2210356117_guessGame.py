import random

# Guessing game! Pick a number randomly. While user does not guess the number correctly give an instruction about the
# number and take another guess from user.
# Instruction:
#
# If the guessed number is lower than the picked number print
# «increase your number»
# else print
# «decrease your number»

number = random.randint(1, 30)
correct = False

while not correct:
    guess = int(input("enter a number: "))
    if guess < number:
        print("«increase your number»")
    elif guess > number:
        print("«decrease your number»")
    else:
        print("You guessed correctly!")
        correct = True

