"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""



def main ():
    choice = int ( input ("Choose a number: "))
    sequence = 1
    flag = True

    while flag:
        multiply = sequence * choice
        print (f"{sequence} * {choice} = {multiply}")
        if multiply > 100:
            break
        else:
            sequence += 1



if __name__ == '__main__':
    main ()
