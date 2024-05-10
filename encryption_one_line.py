
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""


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

    """
    for rch in regular_chars:
        if rch != lower_txt:
            return lower_txt
        
        elif rch == lower_txt:
            rch_index = regular_chars.index(rch)
            ech_found = encrypted_chars[rch_index]
            encripted = lower_txt.replace(lower_txt[0], ech_found)

            if is_lower:
                return encripted
            else:
                return encripted.upper()
        else:
            pass
            
    """
def row_encryption(text):
    """
    Sentence to be Encrypted using ROT13 by encrypt function.

    :param text: str,  string to be send to encrypted
    :return: nothing
    """

    result = ""

    for ch in text:
        x = encrypt(ch)
        result += x


    return result
    
       

def main():
    #output = encrypt("?")
    output = row_encryption("Happy, happy, joy, joy!")

    print(output)

 



if __name__ == "__main__":
    main()









