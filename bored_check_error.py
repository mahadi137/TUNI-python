"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""



def main ():
    flag = True
    while flag:
        Answer = input ("Answer Y or N: ")
        up_ans = Answer.upper ()

        if up_ans == "Y" or up_ans == "N":
            print (f"You answered {Answer}")
            break
        else:
            print ("Incorrect entry.")




if __name__ == '__main__':
    main ()

