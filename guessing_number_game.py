#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program guesses random numbers


import random


def main():
    # this function guesses random numbers

    # input
    integer_as_string = input("Enter the number(1 ~ 10): ")
    some_variable = random.randint(1, 10+1)  # a number between 1 and 10

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        for loop_counter in range(integer_as_number + 1):
            if some_variable == integer_as_number:
                break
            else:
                print("It is wrong")
                integer_as_number = input("Try one more time! (1 ~ 10): ")
        print("It is correct!")
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
