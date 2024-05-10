
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def longest_substring_in_order(text):
    """
    The function longest_substring_in_order, which takes a string as its parameter 
    and searches for the longest substring with its characters in alphabetic order and then returns it.

    :param text: str, the text in which longest_substring will be search.
    :return text: str, the longest substring.
    """
    substr_list = []
    substr = ""
    ch = ""

    #if single character and empty string
    if len(text) == 1 or len(text) == 0:
        return text
    
    #if text length is biggern than 1
    else:
        for i in range(len(text)):
            if text[i] > ch:
                substr += text[i]
                ch = text[i] 

                #if ch is the last in string
                if i == len(text)-1:
                    substr_list.append(substr)

                    return max(substr_list, key=len)

            else:
                #substr += text[i]   
                substr_list.append(substr)
                substr = ""
                substr = text[i]
                ch = text[i]
                #continue

        #comparing and return bigger substr
        return max(substr_list, key=len)

   
    
       

def main():
    substr_long = longest_substring_in_order("abcdefghijklmefghijklmnopopqefgabcde")
    print(substr_long)
  



if __name__ == "__main__":
    main()









