from math import pi


def area_from_radius(r):
    return pi * r ** 2


def area_from_diameter(d):
    return pi * (d / 2) ** 2


def area_or_perimeter():
    choice = input("Do you want to calculate the area or perimeter of a circle? (A) area (P) perimeter").strip().lower()


def calculate_circle_area():
    choice = input("Calculate area using (R) radius or (D) diameter? ").strip().lower()
    if choice == 'r':
        r = float(input("Enter the radius: "))
        return area_from_radius(r)
    elif choice == 'd':
        d = float(input("Enter the diameter: "))
        return area_from_diameter(d)
    else:
        print(" Invalid choice — please enter 'R' or 'D'.")
        return None


def main():
    while True:
        area = calculate_circle_area()
        if area is not None:
            print(f"The area is {area:.4f}")
        again = input("Calculate another circle? (Y/N): ").strip().lower()
        if again != 'y':
            break  # exit the loop


if __name__ == "__main__":
    main()
