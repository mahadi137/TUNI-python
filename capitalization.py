
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def capitalize_initial_letters(word):
    """
    convert the word/name first ch into capitalized.
    :parameter name: str.
    :return ch: str.
    """
    ch = []
    name_list = word.lower().split(" ")

    for w in name_list:
        new_word = w.title()
        ch.append(new_word)
    
    return " ".join(ch)






def main():
    output = capitalize_initial_letters("")

    print(output)
 



if __name__ == "__main__":
    main()









