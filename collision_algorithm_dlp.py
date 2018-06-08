# This program uses a collision algorithm to solve the discrete log problem (DLP).
# Input is a problem of the form: a^x ≡ b mod N, a is the first argument, b is the second, N is the third,
# and the fourth is a user-chosen k value that will be used to populate the second list.
# k should be the floor of the square root of the modulus.

import math


def collision(base, answer, modulo, k):
    first_list = list(base ** x % modulo for x in range(100))
    power = (mod_inverse(base, modulo) ** k) % modulo
    second_list = list(((answer * (power ** y)) % modulo) for y in range(100))
    print("Input: " + str(base) + "^x ≡ " + str(answer) + " mod " + str(modulo) + ", k = " + str(k) + "\n")
    for first_list_element in first_list:
        for second_list_element in second_list:
            if first_list_element == second_list_element:
                print(str(base) + "^" + str(int(first_list.index(first_list_element))) + " ≡ " + str(
                    first_list_element) + " mod " + str(modulo))
                print(str(answer) + "*" + str(base) + "^" + str(
                    int(second_list.index(second_list_element)) * -k) + " ≡ " + str(
                    second_list_element) + " mod " + str(modulo))
                print(str(base) + "^" + str((second_list.index(second_list_element) * k + int(
                    first_list.index(first_list_element)))) + " ≡ " + str(
                    base ** (second_list.index(second_list_element) * k + int(
                        first_list.index(first_list_element))) % modulo) + " mod " + str(modulo))
                print("x = " + str((second_list.index(second_list_element) * k + int(
                    first_list.index(first_list_element)))))
                return
    print("No solution.")


# Mod inverse algorithm from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
##########################################################
def mod_inverse(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcd(b % a, a)
        return g, x - (b // a) * y, y


###########################################################
print("Enter the discrete log problem you wish to solve of the form: a^x ≡ b mod N.")
base = int(input("What is your base (a)? "))
answer = int(input("What is your solution (b)? "))
modulo = int(input("What is your modulus (N)? "))
print("Recommended k value is the floor of the square root of the modulus N: " + str(int(math.sqrt(modulo))))
k = int(input("What is your k value? This is needed for the collision algorithm. "))
collision(base, answer, modulo, k)
