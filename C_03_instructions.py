# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
        This program can calculate the area and/or perimeter of a shape, the available shapes include:
        rectangle, circle, triangle, parallelogram. You will be asked the shape you want to calculate and the numbers
        you want to input.C_03_instructions.py

    ''')
