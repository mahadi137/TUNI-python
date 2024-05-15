"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

# Commands known to the program as global constants.
ADD_COMMAND = "1"
UPDATE_COMMAND = "2"
REMOVE_COMMAND = "3"
PRINT_COMMAND = "4"
QUIT_COMMAND = "5"

# An error message for an missing element as a global constant.
MISSING_MESSAGE = "Name not in the phone book!"

def add_entry(phone_book):
    """Add a new entry to the phone book, if it is not already in the book.

    :param name: dict, the phone book.
    """
    # Read the inputs from the user.
    name = input("Enter a name: ")
    phone_number = input("Enter a phone number: ")

    # Add to the phone book.
    if name not in phone_book:
        phone_book[name] = phone_number
    # Print an error message.
    else:
        print("Entry already in the phone book!")

def update_entry(phone_book):
    """Update a phone number, if it is in the book.

    :param name: dict, the phone book.
    """
    # Read the inputs from the user.
    name = input("Enter a name: ")
    phone_number = input("Enter a new phone number: ")

    # Update the number.
    if name in phone_book:
        phone_book[name] = phone_number
    # Print an error message.
    else:
        print(MISSING_MESSAGE)

def remove_entry(phone_book):
    """Remove an entry from the phone book, if it is in the book.

    :param name: dict, the phone book.
    """
    # Read the name from the user.
    name = input("Enter a name: ")

    # Remove from the book.
    if name in phone_book:
        del phone_book[name]
    # Print an error message.
    else:
        print(MISSING_MESSAGE)

def read_choice():
    """Read a choice from the user and return it.

    :return: str, user's choice.
    """
    # Let us assume that the user is wrong, as always.
    invalid_input = True

    # Read input, while it is invalid.
    while invalid_input:
        msg = ADD_COMMAND + ") Add, " + UPDATE_COMMAND + ") Update, " + \
        REMOVE_COMMAND + ") Remove, " + PRINT_COMMAND + ") Print and " + \
        QUIT_COMMAND + ") Quit: "
        print(msg)
        choice = input("Please, enter your selection: ")
        # A shorter alternative for a conditional expression applying
        # comparisons and logigal operators.
        if choice in (ADD_COMMAND, UPDATE_COMMAND, REMOVE_COMMAND,
        PRINT_COMMAND, QUIT_COMMAND):
            invalid_input = False
        else:
            print("Invalid choice!")

    # Return user's choice.
    return choice

def print_book(phone_book):
    """Print the phone book. Does nothing, if the book is empty.

    :param name: dict, the phone book.
    """
    for name in phone_book:
        print(name, phone_book[name])

def main():
    # The book is empty at the start.
    phone_book = {}

    # Call functions until the user has had enough.
    do_the_loop = True
    while do_the_loop:
        # Decide what to do.
        choice = read_choice()
        if choice == ADD_COMMAND:
            add_entry(phone_book)
        elif choice == UPDATE_COMMAND:
            update_entry(phone_book)
        elif choice == REMOVE_COMMAND:
            remove_entry(phone_book)
        elif choice == PRINT_COMMAND:
            print_book(phone_book)
        elif choice == QUIT_COMMAND:
            do_the_loop = False

if __name__ == "__main__":
    main()