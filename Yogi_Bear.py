"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""
def repeat_name(fname, reps):
    """Repeat name with Bear text"""
    

    for rep in range(0, reps):
        result = ", ".join([fname] * 2)
        print(result, "Bear")



def verse(text, name):
    """for complete text print"""
    
    print(text)
    print(name, name, sep=", ")
    print(text)
    repeat_name(name, 3)
    print(text)
    repeat_name(name, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")
    


if __name__ == "__main__":
    main()
