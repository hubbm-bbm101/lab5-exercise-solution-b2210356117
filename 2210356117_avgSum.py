#  Write a program that asks for a number N as a user input, and calculates the sum of odd numbers, and the average of
#  even numbers starting from 1 up to and including N.


def avg_number(N):
    avg = N/2 + 1
    return avg


def sum_number(N):
    sum = ((N+1)/2) ** 2
    return sum


number = int(input("enter a number (>0): "))
if number % 2 == 0:
    answer = avg_number(number)
    print("the average of even numbers 1 to " + "N is: " + str(answer))
elif number % 2 == 1:
    answer = sum_number(number)
    print("the sum of odd numbers 1 to " + "N is: " + str(answer))

