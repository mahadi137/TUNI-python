"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def ask_num(prompt = ""):
    """
    get number from user
    :param prompt: str
    :return user_entry: int
    """
    user_entry = int(input(prompt))
    return user_entry


def input_to_list(user_number):
    """
    get numbers and add to list
    :param user_number: int
    :return num_list: int list 
    """
    num_list = []
    
    #get numbers from user
    print(f"Enter {user_number} numbers: ")

    for i in range(0, user_number):
        number = ask_num()
        num_list.append(number)

    return num_list



def print_num_search(num_list):
    """
    get which number need to be search and print how many numbers are there
    :param num_list: int list
    :return: nothing
    """

    count = 0
    #USER choice for number search
    user_num_search = int(ask_num("Enter the number to be searched: "))
   
    #count
    count = num_list.count(user_num_search)

    if count == 0:
        print(f"{user_num_search} is not among the numbers you have entered.")
    else:
        print(f"{user_num_search} shows up {count} times among the numbers you have entered.")



def main():
    #user want to process how many numbers?
    user_number = int(ask_num("How many numbers do you want to process: "))

    list_of_num = input_to_list(user_number)
    print_num_search(list_of_num)


if __name__ == "__main__":
    main()
