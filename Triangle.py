"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def calculate_angle(a = 0, b = 90):
    """
    Print top angle of a triangle.
    :param a, b: b default value 90
    :return: nothing
    """
    c = 180 - (a + b)
    
    return c
    


def main():
    left = int(input("Enter the left angle: "))
    right = int(input("Enter the right angle: "))
    
    result = calculate_angle(left, right)
    print(result)    


if __name__ == "__main__":
    main()