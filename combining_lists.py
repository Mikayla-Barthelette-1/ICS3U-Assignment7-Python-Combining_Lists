#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program combines 2 different lists


def combining_the_lists(first_list, second_list):
    # this function combines the lists

    third_list = []

    third_list = first_list + second_list

    return third_list


def main():
    # this function calls other functions

    first_list = []
    second_list = []

    # input
    first_list = input(
        "Please enter your first set of characters you would like combined"
        " (please put a space after the last character): "
    )
    second_list = input(
        "Please enter your second set of characters you would like combined: "
    )

    combined_list = combining_the_lists(first_list, second_list)
    print("\nYour new set of characters is [{0}]".format(combined_list))
    print("\nDone.")


if __name__ == "__main__":
    main()
