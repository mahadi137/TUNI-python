"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def read_input(askInput):
    """Get user input for width and height"""
    while True:
        userInput = int(input(askInput))
        if userInput > 0:
            return userInput

def print_box(width, height, mark):
    """print a box with your mark"""
    for i in range (0, height):
        print(width*mark, end="")
        print()


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()


    print_box(width, height, mark)


if __name__ == "__main__":
    main()



