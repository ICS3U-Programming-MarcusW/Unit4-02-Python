#!/usr/bin/env python3
# Created by: Marcus Wehbi
# Created on: Nov 2, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the
# factorial.


def main():
    # initializations (loop-counter and the answer)
    loop_counter = 0
    factorial_answer = 1

    # get the user number as string
    user_number_as_string = input("Enter a positive number: ")
    # skip a line
    print("")

    try:
        # convert the input to an integer
        user_number_as_int = int(user_number_as_string)
    except ValueError:
        # if error is met, tell the user they didn't properly input a number
        print("{} is not a valid number.".format(user_number_as_string))
    else:
        if user_number_as_int > 0:
            # If the users numbers greater than 0, continue with program
            # replicates a do..while loop
            # calculate the factorial of the user number using a loop
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through a loop.".format(loop_counter))
                if loop_counter >= user_number_as_int:
                    break

            print("")
            # print the answer
            print("{}! = {}".format(user_number_as_int, factorial_answer))
        elif user_number_as_int == 0:
            # 0! is 1, tell the user if the enter 0
            print("0! = 1")
        else:
            # if the number isn't positive, tell the user
            print("{} is not a positive number.".format(user_number_as_int))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
