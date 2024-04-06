"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def read_integer(prompt, minval, maxval):
    """
    function ask for user inputs for year, month and day
    param: text, minval and maxval
    return: int 
    """
    while True:
        result = int(input(f"{prompt} [{minval}-{maxval}] "))

        if minval <= result <= maxval:
            return result
        else:
            print(f"You entered a bad value (must be between {minval}-{maxval})")



def read_inputs():
    """
    function read user inputs for year, month and day
    param: nothing
    return: int 
    """
    year = read_integer("Please enter year: ", 1900, 2500)
    month = read_integer("Please enter month: ", 1, 12)
    day = read_integer("Please enter day: ", 0, 6)

    return year, month, day


def print_calender(year, month, start_day):
    """
    function print calender
    loop through the days
    param: year, month, start_day
    return: nothing
    """

    MON, SUN =  0, 6

    #print header
    print()
    print(f"{year}-{month:02d}")
    print("Mo Tu We Th Fr Sa Su")
    
    #print filler spaces
    print(" " * 3 * start_day, end="")

    #calculate days
    number_of_days = calculate_month_length(month, year)
    current_day = start_day

    #loop through the days and print the calender
    for day in range(1, number_of_days + 1):
        print(f"{day:2} ", end="")

        if current_day == SUN:
            print()
            current_day = MON
        else:
            current_day += 1



def calculate_month_length(month, year):
    """
    function determine months total length
    param: year, month
    return: int
    """

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28



def is_leap_year(year):
    """
    function determine leap year
    param: year
    return: boolean
    """

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0



def main():
    #get inputs
    year, month, day = read_inputs()

    #print calender
    print_calender(year, month, day)



if __name__ == "__main__":
  main()
