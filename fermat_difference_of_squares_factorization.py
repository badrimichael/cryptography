import math


def fermat_difference_of_squares_factorization(n):
    x = int(math.sqrt(n)) + 1
    for i in range(x, x + 1000):
        result = math.sqrt((i ** 2) % n)
        if result.is_integer():
            result = int(result)
            perfect_square = int(n + result ** 2)
            square_root = int(math.sqrt(perfect_square))
            first_factor = square_root + result
            second_factor = square_root - result
            if first_factor * second_factor == n:
                print(str(n) + " + " + str(result) + "^2 = " + str(perfect_square))
                print("Square root " + str(perfect_square) + " = " + str(square_root))
                print(
                    str(n) + " = (" + str(square_root) + "^2 - " + str(result) + "^2) = (" + str(square_root) + " + " +
                    str(result) + ")(" + str(square_root) + " - " + str(result) + ") = " + str(first_factor) + " x " +
                    str(second_factor))
                return
    print("Computation timed out.")


print("Fermat Difference of Squares Factorization:\n" +
      "Note that this program is only meant to showcase the factorization algorithm.\n"
      + "This is not a general-use factorization program. "
        "Source code available here: https://github.com/badrimichael/cryptography.")
user_input = int(input("Enter the integer you would like to factor.\n"))
if user_input <= 1:
    print("Please enter an integer greater than 1.")
else:
    fermat_difference_of_squares_factorization(user_input)
