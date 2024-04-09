"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""
import math


def read_input(prompt):
    """
    get input by user
    :param prompt: str. Request to enter value to calculate
    :return: float, user input or inputs.
    """
    while True:
        value = float(input(prompt))

        if value > 0:
            return value


def print_output(value1, value2):
    """
    Print circumference and area up to two decimal
    :param value1, value2: float. Value upto two decimal 
    :return: nothing
    """

    print(f"The circumference is {value1:.2f}")
    print(f"The surface area is {value2:.2f}")



def square_circum():
    """
    Ask square side length
    :param: nothing
    :return: nothing
    """  
    square_side = read_input("Enter the length of the square's side: ")

    return square_side


def rect_circum():
    """
    Ask rectangle sides length
    :param: nothing
    :return: nothing
    """  
    side_1 = read_input("Enter the length of the rectangle's side 1: ")
    side_2 = read_input("Enter the length of the rectangle's side 2: ")

    return side_1, side_2


def circle_circum():
    """
    Ask circle radius length
    :param: nothing
    :return: nothing
    """  
    radius = read_input("Enter the circle's radius: ")

    return radius


def calcu_sq_circum():
    """
    Calculate square circumference and print
    :param: nothing
    :return: nothing
    """  
    sq_one_side = square_circum()

    sq_circum_result = sq_one_side * 4
    sq_surface_area = sq_one_side * sq_one_side

    print_output(sq_circum_result, sq_surface_area)           



def calcu_rect_circum():
    """
    Calculate rectangle circumference and print
    :param: nothing
    :return: nothing
    """  
    side_1, side_2 = rect_circum()

    rect_circum_result = (side_1 * 2) + (side_2 * 2)
    rect_surface_area = side_1 * side_2

    print_output(rect_circum_result, rect_surface_area)

            

def calcu_circle_circum():
    """
    Calculate circle circumference and print
    :param: nothing
    :return: nothing
    """  
    radius = circle_circum()

    circle_circum_result = 2 * math.pi * radius
    circle_surface_area = math.pi * radius * radius

    print_output(circle_circum_result, circle_surface_area)




def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    :param: nothing
    :return: if 'q' then return to exit loop. Otherwise nothing
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            calcu_sq_circum()

        elif answer == "r":
            calcu_rect_circum()

        elif answer == "c":
            calcu_circle_circum()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()

def main():
    menu()
    print("Goodbye!")

if __name__ == "__main__":
    main()
