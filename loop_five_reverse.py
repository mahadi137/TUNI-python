"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def ask_num(prompt):
    """
    get number from user
    :param prompt: str
    :return user_entry: int
    """
    user_entry = int(input(prompt))
    return user_entry

def get_num():
    """
    Loop and sort is number is larger than zero
    :param: nothing
    :return: nothing
    """
    num_list = []
    print("Give 5 numbers: ")
    
    for i in range(0, 5):
        number = ask_num("Next number: ")
        num_list.append(number)

   
    num_list.reverse()

    print(f"The numbers you entered, in reverse order: ")

    for x in range(0, len(num_list)):
        print(num_list[x])


def main():
    get_num()


if __name__ == "__main__":
    main()
