"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""
def ask_time(prompt):
    """prompt message and get user desired time"""
    return int(input(prompt))


def get_index(bus_time_list, get_user_time):
    """return the index number in the list"""
    length = len(bus_time_list)
    user_time = get_user_time

    for i in range(0, length):
        if user_time <= bus_time_list[i]:
            
            return i
        
    return 0



def get_next_bus(bus_time_list, index_in_list):
    """Find next buss departing time schedule""" 
    next_bus_list = bus_time_list[index_in_list:] + bus_time_list[:index_in_list]

    return next_bus_list[:3]

            

def bus_schedule_check(bus_time_list, get_user_time):
    """Function to check bus shcedule and return next bus list"""
    index_in_list = get_index(bus_time_list, get_user_time)    
    next_bus = get_next_bus(bus_time_list, index_in_list)
    
    return next_bus



def main():
    bus_time_list = [630, 1015, 1415, 1620, 1720, 2000]
    get_user_time = ask_time("Enter the time (as an integer): ")
    next_buses = bus_schedule_check(bus_time_list, get_user_time)

    print("The next buses leave: ")
    for bus in next_buses:
        print(bus)




if __name__ == "__main__":
    main()


