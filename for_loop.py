"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():
    #ask for number to play
    #convert to integer value form string
    nchoice = int (input ("How many numbers would you like to have? "))
    #repetition = 1

    for choice in range (1, nchoice  + 1):

        if choice % 3 == 0 and choice % 7 == 0:
            print ("zip boing")
        elif choice % 3 == 0:
            print ("zip")
        elif choice % 7 == 0:
            print ("boing")
        else:
            print (choice)



if __name__ == "__main__":
    main()
    

