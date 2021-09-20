#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to guess a number between 0 - 9

import random


def main():
    # this tells the user if they picked the right number

    # input
    random_number = int(input("Enter a number between 0 - 9 : "))
    some_variable = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    if random_number == some_variable:
        print("You guessed the number correctly!")
        print("Done.")

    else:
        print("You guessed the number incorrectly :(")
        print("Done.")


if __name__ == "__main__":
    main()
