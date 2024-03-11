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

'''
Bored? (y/n) o
Incorrect entry.
Bored? (y/n) z
Incorrect entry.
Bored? (y/n) m
Incorrect entry.
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) n
Bored? (y/n) f
Incorrect entry.
Bored? (y/n) j
Incorrect entry.
Bored? (y/n) y
Well, let's stop this, then.
'''