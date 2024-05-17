"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():
    filename = input("Enter the filename containing the numbers: ")

    try:
        file = open(filename, mode="r")

    except OSError:
        print(f"Error: opening the file '{filename}' failed!")
        return

    sum_total = 0

    for file_line in file:

        file_line = file_line.rstrip()

        # We have to convert the string representation file_line of
        # the real number to an actual float type value so we can do
        # calculations with it on line 37.  This happens simply by
        # using the function float as we have done many times before.
        # If it so happens tha the line read from the file doesn't
        # represent a float, ValueError excetion will be raised.

        try:
            number = float(file_line)

        except ValueError:
            print(f"Error: the value '{file_line}' is not a float!")
            return

        sum_total += number

    file.close()

    print(f"The sum of all the numbers in {filename} is {sum_total}.")


if __name__ == "__main__":
    main()