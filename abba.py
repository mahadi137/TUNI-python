
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def count_abbas(text):
    """
    Counts the number of occurrences of the substring 'abba' in the given text.
    It counts both overlapping and non-overlapping occurrences. For example, in the string 'abbaabba'.

    :param text: str, the text in which to count occurrences of 'abba'
    :return: int, the number of occurrences of 'abba' in the text
    """
     
    count = 0
    for i in range(len(text)):

        if text[i] == "a":
            ch_index = i
            if text[ch_index:ch_index+4] == "abba":
                count += 1
                
    return count

   
    
       

def main():
    count = count_abbas("abb")
    print(count)
  
 
 



if __name__ == "__main__":
    main()









