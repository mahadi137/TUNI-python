"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""



def main ():
    feel = int (input ('How do you feel? (1-10) '))

    if feel > 10 or feel < 1:
        print ('Bad input!')
    else:
        if feel == 1:
            print ("A suitable smiley would be :'(")
        elif feel == 10:
            print ("A suitable smiley would be :-D")
        elif feel > 7:
            print ('A suitable smiley would be :-)')
        elif feel < 4:
            print ('A suitable smiley would be :-(')
        else:
            print ('A suitable smiley would be :-|')


if __name__ == '__main__':
    main ()



