"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    Print a box
    :param height, width, border_mark="#", inner_mark=" ": int and str
    :return: nothing
    """
    
    for i in range(1, height+1):
        for j in range(1, width+1):
        
            if (i==1 or i==height or j==1 or j==width):
                print(border_mark, end="")

            else:
                print(inner_mark, end="")
        print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
