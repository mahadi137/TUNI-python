
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""


def is_the_list_in_order(num_list):
    """
    information about the function goes here
    :param num_list: int list
    :return: nothing
    """

    if num_list == [] or len(num_list) == 1:
        return True
    else:
        list1 = num_list

        for i in range (0, len(list1)-1):
            if list1[i] > list1[i+1]:
                return False
        return True
            
    

    


def main():
    boolean_output = is_the_list_in_order([1, 2, 5, 6,7, 9])

    print(boolean_output)
   


if __name__ == "__main__":
    main()
