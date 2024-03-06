"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""




def main():
    #ask for number to play
    #convert to integer value form string
    nchoice = int (input ("How many numbers would you like to have? "))
    repetition = 1

    while repetition <= nchoice:

        if repetition % 3 == 0 and repetition % 7 == 0:
            print ("zip boing")
        elif repetition % 3 == 0:
            print ("zip")
        elif repetition % 7 == 0:
            print ("boing")
        else:
            print (repetition)

        repetition +=1











if __name__ == "__main__":
    main()
    