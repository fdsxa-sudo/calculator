import math


# Functions go here
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    while True:
        response = input(question).lower()
        for item in valid_answers:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}")


def int_check(question, low, high):
    error = f"Oops - please enter a number between {low} and {high}."
    while True:
        response = input(question).lower()
        if response == "xxx":
            return response
        try:
            response = int(response)
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def make_statement(statement, decoration):
    print(f"{decoration * 3} {statement} {decoration * 3}")


def instructions():
    make_statement("Instructions", "ℹ️")
    print('''
    This program can calculate the area and/or perimeter of a shape.
    Available shapes include:
    rectangle, square, triangle, parallelogram, or circle.

    You will be asked what shape and what you want to calculate.
    Type "xxx" to exit at any input.
    ''')


# Ask for instructions
want_instructions = string_check("Do you want to see the instructions? ")
if want_instructions == "yes":
    print()
    instructions()

# Calculator start
shapes = ["rectangle", "square", "triangle", "parallelogram", "circle"]
history = []

user_choice = input(
    "Which shape do you want to calculate? rectangle, square, triangle, parallelogram, or circle? ").strip().lower()

if user_choice not in shapes:
    print("Invalid shape.")
else:
    calc_choice = string_check("Do you want to calculate area, perimeter, or both? ", ("area", "perimeter", "both"))

    if user_choice == "rectangle":
        length = int_check("Length of rectangle: ", 1, 1000)
        width = int_check("Width of rectangle: ", 1, 1000)

        if calc_choice in ["area", "both"]:
            area = length * width
            print(f"Area = {area}")
            history.append(f"Rectangle Area: {length} x {width} = {area}")
        if calc_choice in ["perimeter", "both"]:
            perimeter = 2 * (length + width)
            print(f"Perimeter = {perimeter}")
            history.append(f"Rectangle Perimeter: 2 x ({length} + {width}) = {perimeter}")

    elif user_choice == "square":
        side = int_check("Side length of square: ", 1, 1000)

        if calc_choice in ["area", "both"]:
            area = side ** 2
            print(f"Area = {area}")
            history.append(f"Square Area: {side}^2 = {area}")
        if calc_choice in ["perimeter", "both"]:
            perimeter = 4 * side
            print(f"Perimeter = {perimeter}")
            history.append(f"Square Perimeter: 4 x {side} = {perimeter}")

    elif user_choice == "triangle":
        side1 = int_check("Length of side 1: ", 1, 1000)
        side2 = int_check("Length of side 2: ", 1, 1000)
        side3 = int_check("Length of side 3: ", 1, 1000)

        if calc_choice in ["area", "both"]:
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            print(f"Area = {area:.2f}")
            history.append(f"Triangle Area (Heron's formula): {area:.2f}")
        if calc_choice in ["perimeter", "both"]:
            perimeter = side1 + side2 + side3
            print(f"Perimeter = {perimeter}")
            history.append(f"Triangle Perimeter: {side1} + {side2} + {side3} = {perimeter}")

    elif user_choice == "parallelogram":
        base = int_check("Base of parallelogram: ", 1, 1000)
        height = int_check("Height of parallelogram: ", 1, 1000)

        if calc_choice in ["area", "both"]:
            area = base * height
            print(f"Area = {area}")
            history.append(f"Parallelogram Area: {base} x {height} = {area}")
        if calc_choice in ["perimeter", "both"]:
            side = int_check("Length of the slanted side: ", 1, 1000)
            perimeter = 2 * (base + side)
            print(f"Perimeter = {perimeter}")
            history.append(f"Parallelogram Perimeter: 2 x ({base} + {side}) = {perimeter}")

    elif user_choice == "circle":
        diameter = int_check("Diameter of the circle: ", 1, 1000)
        radius = diameter / 2

        if calc_choice in ["area", "both"]:
            area = math.pi * radius ** 2
            print(f"Area = {area:.2f}")
            history.append(f"Circle Area: π x {radius}^2 = {area:.2f}")
        if calc_choice in ["perimeter", "both"]:
            circumference = math.pi * diameter
            print(f"Perimeter (Circumference) = {circumference:.2f}")
            history.append(f"Circle Perimeter: π x {diameter} = {circumference:.2f}")

# Ask user if they want to save the history
if history:  # Only ask if calculations were made
    save_history = string_check("Do you want to save the calculation history to a file? ")
    if save_history == "yes":
        file_name = "calculator_history"
        with open(f"{file_name}.txt", "w", encoding="utf-8") as text_file:
            text_file.write("=== Calculator History ===\n")
            for item in history:
                text_file.write(item + "\n")
        print(f"Results saved to {file_name}.txt")
    else:
        print("History not saved.")
