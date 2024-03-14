"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    initial_day = 1
    first_friday = '3.1.'
    
                      
    for month in range (1, 13):
        for day in range (1, days_in_months [month - 1] + 1):

            my_format = "{0}.{1}."
            date_format = my_format.format(day, month)

            if first_friday == date_format:
                print (date_format)
                initial_day = 0

            initial_day += 1

            if initial_day == 8:
                print (date_format)
                initial_day = 1
                




   

if __name__ == "__main__":
    main()

