"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""
def repeat_name(fname, rep):
    """Repeat name with Bear text"""
    result = ", ".join([fname] * rep)
    print(result, "Bear")



def verse(text, name):
    """for complete text print"""
    
    print(text)
    print(name, name, sep=", ")
    print(text)
    repeat_name(name, 2)
    repeat_name(name, 2)
    repeat_name(name, 2)
    print(text)
    repeat_name(name, 2)
    print()

def main():
    verse("I know someone you don't know", "Yogi")
    verse("Yogi has a best friend too", "Boo Boo")
    verse("Yogi has a sweet girlfriend", "Cindy")
    


if __name__ == "__main__":
    main()
