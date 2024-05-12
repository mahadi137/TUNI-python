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

    parag = ''

    while True:
        row = input()

        if row == '':
            break

        parag += row +' '
    
    return parag



def wrapped_txt(text, ch_per_line):
    """
    This function wraps a given text into multiple lines based on a specified character limit per line.

    :param:
    text (str): The input text to be wrapped.
    ch_per_line (int): The maximum number of characters allowed per line.

    :return:
    word_list (list): A list of strings where each string is a line from the wrapped text.
    """
  
    #get list of word from the paragraph
    text_split = text.split(" ")

    #initialization
    word_list = []
    line = ""

    for word in text_split:
        #when, until total ch per line less than 50
        if len(line + word) <= ch_per_line:
            line += word + " "

            #if last line
            if word == text_split[-1]:
                #last line will append
                word_list.append(line)

        #when ch per line increase 50 ch
        else:
            word_list.append(line)
            #previous line removed and added lates word 
            #from loop with single space
            line = word + " "

    #after loop return list of lines
    #print(word_list)
    return word_list 




def pad_to_chars(word_list, ch_per_line):
    """
    This function takes a list of words and pads each line with spaces to make it exactly 50 characters long.

    :param:
    word_list (list): A list of strings where each string is a line from the text.

    :return:
    None. The function prints out the padded lines directly.
    """

    #final result list
    result_list = []


    for line in word_list:

        words = line.split()

        # whdn last line is the last in given list
        if len(words) == 1:
            #append and add empty spaces at the end
            result_list.append(line.rstrip() + ' ' * (ch_per_line - len(line.rstrip())))
        
        else:
            #calculate how many space needed
            # + line.count(' ') this one is to get toatl desired ch
            total_spaces_needed = ch_per_line - len(line) + line.count(' ')
            spaces_between_words = total_spaces_needed // (len(words) - 1)
            extra_spaces = total_spaces_needed % (len(words) - 1)

            #initial with fist word
            #words will be append in this list
            padded_words = [words[0]]

            for i in range(1, len(words)):
                if i <= extra_spaces:
                    space = ' ' * (spaces_between_words + 1)
                    #word by word add space and append
                    padded_words.append(space + words[i])

                else:
                    space = ' ' * spaces_between_words
                    #add needed space
                    padded_words.append(space + words[i])
                    
            #join words and form line
            joined_line = ''.join(padded_words)
        
        
            result_list.append(joined_line)

    return result_list
    
 


def main():
    #parag = "CHAPTER VIII - CONCERNING THOSE WHO HAVE OBTAINED A PRINCIPALITY BY WICKEDNESS Although a prince may rise from a private station in two ways, neither of which can be entirely attributed to fortune or genius, yet it is manifest to me that I must not be silent on them, although one could be more copiously treated when I discuss republics. These methods are when, either by some wicked or nefarious ways, one ascends to the principality, or when by the favour of his fellow-citizens a private person becomes the prince of his country. And speaking of the first method, it will be illustrated by two examples--one ancient, the other modern--and without entering further into the subject, I consider these two examples will suffice those who may be compelled to follow them."
    
    print("Enter text rows. Quit by entering an empty row.")
    parag = read_message()
    
    ch_per_line = int(input("Enter the number of characters per line: "))

    word_list = wrapped_txt(parag, ch_per_line)
    result = pad_to_chars(word_list, ch_per_line)
  
    #print each formated line
    for line in result:
        print(line)




if __name__ == "__main__":
    main()
