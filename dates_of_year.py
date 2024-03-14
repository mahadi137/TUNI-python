"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in range (1, 13):
        for day in range (1, days_in_months [month - 1] + 1):
            print (day, ".", month, ".", sep = "")


   

if __name__ == "__main__":
    main()

