"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():

    # Starts by asking the user the number of days they want to analyze
    days_of_jogg = int (input ("Enter the number of days: "))

    # store km in list
    KM_list = []
    total_KM = float (0.00)
    lazy_day_count = 0

    for day in range (1, days_of_jogg + 1):
        jogged_km = float (input (f"Enter day {day} running length: "))
        if jogged_km == 0:
            lazy_day_count += 1
            if lazy_day_count == 3:
                 # a blank line
                print()
                print ("You had too many consecutive lazy days!")
                return
        else: 
            if jogged_km != 0:
                lazy_day_count = 0
                KM_list.append (jogged_km)
        


    # loop and get total km
    for km in KM_list:
        total_KM += km

        


    # Analyze jogged data
    avg_KM = total_KM / days_of_jogg



    # give feedback
    # a blank line
    print()
    # km too low
    if avg_KM > 3:
        print (f"You were persistent runner! With a mean of {avg_KM:1.2f} km.") 
    # km avobe 3km
    else: print (f"Your running mean of {avg_KM:1.2f} km was too low!")

    



if __name__ == "__main__":
    main()

