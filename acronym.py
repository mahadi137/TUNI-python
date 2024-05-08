"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def create_an_acronym(name):
    """
    convert the word/name into acronym.
    :parameter name: str.
    :return word: str.
    """
    ch = []
    name_list = name.split(" ")

    for word in name_list:
        sliced_ch = word[0].upper()
        ch.append(sliced_ch)
    
    return "".join(ch)






def main():
    output = create_an_acronym('my name is')

    print(output)
 



if __name__ == "__main__":
    main()