# This program factors a positive integer given by the user using Pollard's p-1 algorithm.
# Input is a positive integer greater than 2.

from math import factorial, gcd

# Algorithm calculates up to 10!.
def pollard(n):
    for _ in range(1, 10):
        if gcd(((2 ** factorial(_)) % n) - 1, n) != 1:
            first_factor = gcd(((2 ** factorial(_)) % n) - 1, n)
            second_factor = n // first_factor
            if first_factor == n:
               continue
            print("Factor found via " + str(_) + "!")
            print(str(n) + " = " + str(first_factor) + " x " + str(second_factor))
            return
    print("Computation timed out. Your integer may be prime, too large, or p-1 may have a large prime factor.")

print("Pollard's p-1 Factorization:\n" +
"Note that the computation times out at 10! and this program is only meant to showcase the factorization algorithm.\n"
+ "This is not a general-use factorization program. Source code available here: https://github.com/badrimichael/cryptography.")
user_input = int(input("Enter the integer you would like to factor.\n"))
if user_input <= 2:
    print("Please enter an integer greater than 2.")
else:
    pollard(user_input)
