"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

from math import sqrt

def area(a,b,c):
    """calculate triangle area"""
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    return A


def main():
    a = float(input("Enter the length of the first side: "))
    c = float(input("Enter the length of the second side: "))
    b = float(input("Enter the length of the third side: "))

    area_result = area(a,b,c)

    print(f"The triangle's area is {area_result:1.1f}")


if __name__ == "__main__":
    main()
