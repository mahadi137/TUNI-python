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
    

"""
def main():
    hero_level = 1
    for hero_name in [ "RoboCop (1987)", "Saitama", "D. Vader", "R. Sanchez" ]:
        print("My favorite superhero number", hero_level, "is", hero_name)
        hero_level += 1

if __name__ == "__main__":
    main()

    
    print(*range(1, 10, 2))        # printout: 1 3 5 7 9
    print(*range(100, 200, 10))    # printout: 100 110 120 130 140 150 160 170 180 190
    print(*range(1900, 2021, 20))  # printout: 1900 1920 1940 1960 1980 2000 2020

"""