"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""
def main ():

    #money change
    # Initialize counters for each denomination
    ten_euro_notes = 0
    five_euro_notes = 0
    two_euro_coins = 0
    one_euro_coins = 0

    #asking
    purchase = int (input ("Purchase price: "))
    paid_amount = int (input ("Paid amount of money: "))

    
    change = paid_amount - purchase

    #condition
    if change >= 10:
        ten_euro_notes = change // 10
        change %= 10

    if change >= 5:
        five_euro_notes = change // 5
        change %= 5

    if change >= 2:
        two_euro_coins = change // 2
        change %= 2

    if change == 1:
        one_euro_coins = change


    # Print no change
    if paid_amount <= purchase:
        print("No change")
    


    # Print the change breakdown
    if paid_amount > purchase:
        
        print("Offer change:")

        if ten_euro_notes > 0:
            print(f"{ten_euro_notes} ten-euro notes")

        if five_euro_notes > 0:
            print(f"{five_euro_notes} five-euro notes")

        if two_euro_coins > 0:
            print(f"{two_euro_coins} two-euro coins")

        if one_euro_coins > 0:
            print(f"{one_euro_coins} one-euro coins")
    


if __name__ == '__main__':
    main ()


