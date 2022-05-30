#!/usr/bin/env python3

# Created by Noah McCaskill
# Created May 2022
# This program converts degrees celsius to degrees fahrenheit


def conversion():
    # this function converts celsius to fahrenheit

    # input
    celsius_string = input("Enter a temperature (°C): ")

    # process & output
    try:
        celsius = float(celsius_string)

        fahrenheit = (9 / 5) * celsius + 32

        print("\n{0}°C is equal to {1:.1f}°F.".format(celsius_string, fahrenheit))

    except Exception:
        print("\nYour temperature is invalid. Please Re-Run.")

    print("\nDone.")


def main():
    # this function calls the conversion function

    # call function
    conversion()


if __name__ == "__main__":
    main()