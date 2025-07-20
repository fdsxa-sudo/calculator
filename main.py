import math
from math import pi


# Functions go here

def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def int_check(question, low, high):
    """Checks users enter an integer"""

    error = f"Oops - please enter an number between {low} and {high}."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# instructions

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

    This program can calculate the area and/or perimeter of a shape, the available shapes include:
    rectangle, circle, triangle, parallelogram or circle. You will be asked the shape you want to calculate and the 
    /numbers
    you want to input.

    ''')


want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    print(instructions())
