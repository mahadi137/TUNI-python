"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""


def compare_floats(num1, num2, EPSILON):
    """Calculate and return True or false.

    :param num1, num2, EPSILON: float, float, float, num1 and num2 will be compared. EPSILON is tolerance
    :return: bool, True if calculation is less than EPSILON else False.
    """

    substract = abs(num1 - num2)
    
    if substract < EPSILON:
        return True
    else: 
        return False


def main():
    EPSILON = 0.000000001
    result = compare_floats(0.00000000000000000001, 0.0000000000000000002, EPSILON)
    print(result)


if __name__ == "__main__":
    main()