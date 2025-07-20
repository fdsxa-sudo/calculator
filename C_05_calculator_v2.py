import math


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
    rectangle, circle, triangle, parallelogram or circle. 
    You will be asked the shape you want to calculate and the numbers you want to input. 
    You can also type "xxx" to exit the code.

    ''')


want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    print()
    print(instructions())

# calculator


shapes = ["rectangle", "square", "triangle", "parallelogram"]

user_choice = input("Which of these shapes do you want to calculate? rectangle, square, "
                    "triangle or parallelogram? ").strip().lower()
if user_choice == "rectangle":
    answer_rectangle_side_1 = int_check("What is the lengths of side one? ", 1, 1000)
    answer_rectangle_side_2 = int_check("What is the length of side two? ", 1, 1000)

    answer_rectangle = answer_rectangle_side_1 * answer_rectangle_side_2
    print(answer_rectangle)

elif user_choice == "square":
    answer_square_side = int_check("What is the length of a side of the square?", 1, 1000)

    answer_square = answer_square_side * answer_square_side
    print(answer_square)

elif user_choice == "triangle":
    answer_triangle_side_1 = int_check("What is the length of side one? ", 1, 1000)
    answer_triangle_side_2 = int_check("What is the length of side two? ", 1, 1000)
    answer_triangle_side_3 = int_check("What is the length of side three? ", 1, 1000)

elif user_choice == "parallelogram":
    answer_parallelogram_height = int_check("What is the height of the shape? ", 1, 1000)
    answer_parallelogram_width = int_check("What is the width of the shape? ", 1, 1000)
    answer_parallelogram = 2 * (answer_parallelogram_width + answer_parallelogram_height)
    print(answer_parallelogram)

elif user_choice == "circle":
    answer_circle_diameter = int_check("What is the diameter", 1, 1000)
    answer_circle = 2 * answer_circle_diameter * math.pi
    print(answer_circle)

# write to file code

# create file to hold data (add .txt extension)
file_name = "calculater_history"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# strings to write file...
heading = "=== Calc ===\n"
content = "Random content"
more = "A bit more content"

# list of strings...
to_write = [heading, content, more]

# print the output
for item in to_write:
    print(item)

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
