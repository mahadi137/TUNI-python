"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():
    flag = True

    while flag:
        choice = input ("Bored? (y/n) ").lower ()

        while choice == "n":
            choice = input ("Bored? (y/n) ").lower ()

        if choice == "y":
            print ("Well, let's stop this, then.")
            return
        else:
            print ("Incorrect entry.")




if __name__ == "__main__":
    main()