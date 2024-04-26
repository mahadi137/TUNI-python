
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""


def are_all_members_same(num_list):
    """
    information about the function goes here
    :param num_list: int list
    :return: nothing
    """

    if num_list == []:
        return True
    else:
        list1 = num_list
        list2 = sorted(list1, reverse=True)
        return (list1 == list2)

    


def main():
    boolean_output = are_all_members_same([])

    print(boolean_output)
   


if __name__ == "__main__":
    main()
