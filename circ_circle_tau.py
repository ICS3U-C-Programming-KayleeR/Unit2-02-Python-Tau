#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 26,09,2026
# Testing basic math operations
import constants


def main():
    # get the radius of the circle from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference using Tau
    circumference = constants.TAU * radius

    # display the circumference
    print("Circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()
