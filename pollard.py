# This program factors a positive integer given by the user using Pollard's p-1 algorithm.
# Input is a positive integer greater than 2.

from math import factorial, gcd


# Algorithm calculates up to 50!.
def pollard(n):
    for _ in range(1, 50):
        if gcd(((2 ** factorial(_)) % n) - 1, n) != 1:
            first_factor = gcd(((2 ** factorial(_)) % n) - 1, n)
            second_factor = n // first_factor
            print("Factor found via " + str(_) + "!")
            print(str(n) + " = " + str(first_factor) + " x " + str(second_factor))
            break


print("Pollard's p-1 Factorization:")
user_input = int(input("Enter the integer you would like to factor.\n"))
if user_input <= 2:
    print("Please enter an integer greater than 2.")
else:
    pollard(user_input)
