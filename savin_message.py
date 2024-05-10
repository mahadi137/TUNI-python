
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def read_message():
    """
    Reads the input entered by the user, saves the rows in a list, and returns the list.
    The entry of the input is terminated by entering an empty row. This empty row is not saved in list.
    :param: nothing
    :return message: list
    """

    message = []

    while True:
        row = input()

        if row == "":
            break

        message.append(row)
    
    return message




def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    
    for row in msg:
        print(row.upper())


if __name__ == "__main__":
    main()









