"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def loop(num_list):
    """
    Loop through the list
    :param num_list: int list
    :return num: int
    """
    for num in num_list:
        print(num) 


def get_even_num():
    """
    get even number and print ascending, descending order 
    :param: nothing
    :return: nothing
    """

    num = 101
    num_list = []
    
    for i in range(0, num):
        if i%2 == 0:
            num_list.append(i)
            
    #loop ascending order        
    loop(num_list)
    
    #reverse the list
    num_list.sort(reverse=True)

    #loop descending order       
    loop(num_list)



def main():
    get_even_num()


if __name__ == "__main__":
    main()
