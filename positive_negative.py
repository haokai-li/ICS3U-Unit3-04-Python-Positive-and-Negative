#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Sept 2021
# This Program check that the integer is positive, negative and zero


def main():
    # This function check that the integer is positive, negative and zero

    # input
    integer = int(input("Enter an integer: "))
    print("")

    # process
    if integer > 0:
        # output
        print("{} is a positive number.".format(integer))
    elif integer < 0:
        # output
        print("{} is a negative number.".format(integer))
    else:
        # output
        print("{} is just zero.".format(integer))

    print("\nDone")


if __name__ == "__main__":
    main()
