
"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def user_score(prompt):
    """
    Ask for score five times.
    :param prompt: str. text to print
    :return: list
    """
    # empty list
    score_list = []

    # ask score for five times
    for i in range(1, 6):
        score = float(input(f"{prompt}{i}: "))
        score_list.append(score)

    return score_list



def filter(score_list):
    """
    remove max and min score.
    :param score_list: list. five score
    :return: list
    """
    max_value = max(score_list)
    min_value = min(score_list)

    score_list.remove(max_value)
    score_list.remove(min_value)

    return score_list
   

def offc_score(filtered_list):
    """
    Average score of three and print result.
    :param filtered_list: list. three score
    :return: nothing
    """
    result = sum(filtered_list)/len(filtered_list)

    print(f"The official competition score is {result:.2f} seconds.")



def official_score():
    """
    information about the function goes here
    :param: 
    :return: nothing
    """
    performace_score_list = user_score("Enter the time for performance ")
    filtered_list = filter(performace_score_list)

    #print output after average
    offc_score(filtered_list)

   
            


def main():
 official_score()
   


if __name__ == "__main__":
    main()
