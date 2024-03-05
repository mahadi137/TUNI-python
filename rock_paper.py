"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""



def main ():
    player_1 = str (input ('Player 1, enter your choice (R/P/S): '))
    player_2 = str (input ('Player 2, enter your choice (R/P/S): '))


    if player_1 == player_2:
        print ("It's a tie!")

    else:
        if player_1 == 'R':
            if player_2 == 'S':
                print ("Player 1 won!")

        elif player_1 == 'S':
            if player_2 == 'P':
                print ("Player 1 won!")

        elif player_1 == 'P':
            if player_2 == 'R':
                print ("Player 1 won!")

        if player_2 == 'R':
            if player_1 == 'S':
                print ("Player 2 won!")

        elif player_2 == 'S':
            if player_1 == 'P':
                print ("Player 2 won!")

        elif player_2 == 'P':
            if player_1 == 'R':
                print ("Player 2 won!")
        
        else:
            pass


if __name__ == '__main__':
    main ()



