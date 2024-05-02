"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def convert_grades(grades):
    """
    Converters grades which is higher than 0
    :param grades: list. integers to convert
    :return: nothing
    """

    length = len(grades)
    index = 0
    while index < length:
        if grades[index] > 0:
            grades[index] = 6

        index += 1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
