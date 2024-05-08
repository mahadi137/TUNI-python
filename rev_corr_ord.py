"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def reverse_name(fname):
    """
    ask for the word.
    :parameter fname: str.
    :return word: str.
    """
    word = []
    name_list = fname.split(",")
    
    if len(name_list) == 1:
        return fname
    else:
        for i in range(len(name_list)):
            single_word = name_list[i].strip()
            word.append(single_word)

    word[1], word[0] = word[0], word[1]

    return " ".join(word).strip()






def main():
    output = reverse_name('uu')

    print(output)
 



if __name__ == "__main__":
    main()