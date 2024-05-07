"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750

Temperature analyzer program, which will help the user to figure out the warm and 
cold days during the period in which the measurements were made.
"""

def ask_days(prompt):
    """
    prompt message and get user desired days to analyze temperatures.
    :parameter prompt: str.
    :return days: int
    """
    #day always int value
    return int(input(prompt))


def ask_daily_temp(days):
    """
    get daily temperature to analyze.
    :parameter prompt: str.
    :return temp_list: list. float numbers
    """
    #empty list to initialize list
    temp_list = []

    #for loop to prompt daily temp input request
    for day in range(1, days+1):
        #value probably float
        temp = float(input(f"Enter day {day}. temperature in Celsius: "))
        #append in the list
        temp_list.append(temp)

    return temp_list


def find_mean(temp_list):
    """
    Analyze the list temp and return the mean/average value.
    
    :parameter temp_list: list. float numbers
    :return: float.
    """

    #sorting the list, ordered
    sum_of_list = sum(temp_list)

    #get length to find the index
    length = len(temp_list)

    #return mean value
    return sum_of_list/length

  

def find_median(temp_list):
    """
    Analyze the list temp and return the median value.
    -When the number of measurements is odd, the median is the middle element of the sorted list of the measurements.
    -If the number of measurements is even, the median is the mean of the two middle elements of the said sorted list.
    -When there is only one element the median is the value of that element.

    :parameter temp_list: list. float numbers
    :return: float.
    """

    #sorting the list, ordered
    sorted_list = sorted(temp_list)

    #get length to find the index
    length = len(sorted_list)
    index_value = (length-1)//2

    #if list length is even
    if (length%2):
        return sorted_list[index_value]
    #if list length is odd
    else:
        return (sorted_list[index_value] + sorted_list[index_value+1]) / 2.0
    



def over_under_median(temp_list, median_temp, mean_temp):
    """
    Compare listed temp with median temp and divide temp into two group, over/at and under median temp

    :parameter temp_list, median_temp, mean_temp: list, float, float. list contains float.
    :return: nothing
    """

    print("Over or at median were:")

    #for over or at median temp
    for temp in temp_list:
        if temp >= median_temp:
            difference, temp_index = analysis(temp_list, temp, mean_temp)
            print(f"Day{temp_index:3.0f}.{temp:6.1f}C difference to mean:{difference:6.1f}C")

    print()
    print("Under median were:")

    #for under median temp
    for temp in temp_list:
        if temp < median_temp:
            difference, temp_index = analysis(temp_list, temp, mean_temp)
            print(f"Day{temp_index:3.0f}.{temp:6.1f}C difference to mean:{difference:6.1f}C")
         
            


def analysis(temp_list, temp, mean_temp):
    """
    Analyze the list temp and index of temp in the list.

    :parameter temp_list, temp, mean_temp: list, float, float. list contains float.
    :return difference, temp_index: float, int
    """

    difference = temp-mean_temp
    temp_index = temp_list.index(temp)+1
    
    return difference, temp_index




def main():
    days_to_analyze = ask_days("Enter amount of days: ")
    temp_list = ask_daily_temp(days_to_analyze)
    #temp_list = [1.5, 0.2, -5, -25, -3.1, -4.2, -27.7, -12.1, -5.1, 4.2]
    mean_temp = find_mean(temp_list)
    median_temp = find_median(temp_list)
    
    print()
    print(f"Temperature mean: {mean_temp:.1f}C")
    print(f"Temperature median: {median_temp:.1f}C")
    print()
    over_under_median(temp_list, median_temp, mean_temp)



if __name__ == "__main__":
    main()