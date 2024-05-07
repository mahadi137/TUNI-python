"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def ask_word(prompt):
    """
    ask for the word.
    :parameter prompt: str.
    :return word: str.
    """
    given_word = input(prompt).lower()
    word_no_space = given_word.split(" ")
    word = "".join(word_no_space)

    return word


def ck_vol(word):
    """
    Check constant vowel.
    :parameter word: str.
    :return count: int
    """
    count = 0
    vol_list = ['a', 'e', 'i', 'o', 'u', 'y']

    for w in range(len(word)):
        if word[w] in vol_list:
            count += 1

    return count


def ck_const(word):
    """
    Check constant characters.
    :parameter word: str.
    :return count: int
    """
    count = 0
    vol_list = ['a', 'e', 'i', 'o', 'u', 'y']
    
    for w in range(len(word)):
        if word[w] not in vol_list:
            count += 1

    return count



def main():
    word = ask_word("Enter a word: ")
    vowel = ck_vol(word)
    const = ck_const(word)

    print(f"The word \"{word}\" contains {vowel} vowels and {const} consonants.")
    



if __name__ == "__main__":
    main()