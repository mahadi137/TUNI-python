"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def print_verse (animal, sound):
    """Print the song with different animal and different sound"""
    print(f"Old MACDONALD had a farm\nE-I-E-I-O\nAnd on his farm he had a {animal}\nE-I-E-I-O\nWith a {sound} {sound} here\nAnd a {sound} {sound} there\nHere a {sound}, there a {sound}\nEverywhere a {sound} {sound}\nOld MacDonald had a farm\nE-I-E-I-O")
    

def main():
    """main function"""
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")



if __name__ == "__main__":
    main()
