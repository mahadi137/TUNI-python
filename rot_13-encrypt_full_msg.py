
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def read_message():
    """
    Reads the input entered by the user, saves the rows in a list, and returns the list.
    The entry of the input is terminated by entering an empty row. This empty row is not saved in list.
    :param: nothing
    :return message: list
    """

    message = []

    while True:
        row = input()

        if row == "":
            break

        message.append(row)
    
    return message


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  ch to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    #is lower or upper
    is_lower = text.islower()

    lower_txt = text.lower()
    
    #if not in 
    if lower_txt not in regular_chars:
        return lower_txt
    else:
        rch_index = regular_chars.index(lower_txt)
        ech_found = encrypted_chars[rch_index]

        #change ch to lower or upper case
        if is_lower:
            return ech_found
        else:
            return ech_found.upper()


def row_encryption(text):
    """
    Sentence to be Encrypted using ROT13 by encrypt function.

    :param text: str,  string to be send to encrypted
    :return: nothing
    """

    result = []

    for row in text:
        msg_str = ""
        for ch in row:
            en_ch = encrypt(ch)
            msg_str += en_ch
        result.append(msg_str)


    return result
    
       

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    output = row_encryption(msg)

    print("ROT13:")
    for row in output:
        print(row)

 



if __name__ == "__main__":
    main()









