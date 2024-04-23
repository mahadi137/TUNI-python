"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")



def fill(tank_size, gas_fill_req, gas_remain_tank):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    gas_allowed = tank_size - gas_remain_tank

    if gas_fill_req > gas_allowed:
        return gas_allowed
    else:
        return gas_fill_req
    



def drive(prv_x, prv_y, new_x, new_y, gas, gas_consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    
    car_curr_drive_capacity = (100/gas_consumption)*gas  #100km can drive with 10 L gas, where car consumption is 10L per 100km
    car_drive = pythagorean(prv_x, new_x, prv_y , new_y)

    
    if car_curr_drive_capacity < car_drive:
        car_can_not_go = car_drive - car_curr_drive_capacity
        car_drove, reach_new_x, reach_new_y = when_drive_is_high(prv_x, new_x, prv_y , new_y, car_curr_drive_capacity, car_drive)      
        # all capacity taken till now
        gas_remain = km_to_gas_conv(car_curr_drive_capacity, car_drove, gas_consumption)

        return gas_remain, reach_new_x, reach_new_y
    
    else:
        car_drive, reach_new_x, reach_new_y = when_capacity_is_high(prv_x, new_x, prv_y , new_y, car_drive)
        # all capacity taken till now
        gas_remain = km_to_gas_conv(car_curr_drive_capacity, car_drove, gas_consumption)

        return gas_remain, reach_new_x, reach_new_y



def when_drive_is_high(prv_x, new_x, prv_y , new_y, car_curr_drive_capacity, car_drive):
    """
    Implemented just to write less for clean code.
    """

    if prv_x == new_x:
        new_cor_y = car_curr_drive_capacity - abs(prv_y)
        reach_new_x, reach_new_y = new_x, new_cor_y

    if prv_y == new_y:
        new_cor_x = car_curr_drive_capacity - abs(prv_x)
        reach_new_x, reach_new_y = new_cor_x, new_y
    
    car_drove = car_curr_drive_capacity

    return car_drove, reach_new_x, reach_new_y




def when_capacity_is_high(prv_x, new_x, prv_y , new_y, car_drive):
    """
    Implemented just to write less for clean code.
    """

    if prv_x == new_x:
        new_cor_y = car_drive - abs(prv_y)
        reach_new_x, reach_new_y = new_x, new_cor_y

    if prv_y == new_y:
        new_cor_x = car_drive - abs(prv_x)
        reach_new_x, reach_new_y = new_cor_x, new_y

    return car_drive, reach_new_x, reach_new_y
    


def km_to_gas_conv(car_km, car_d_km, gas_conmp):
    """
    calculate remaining car km capacity and convert
    km to gas.
    """
    car_remain_km = abs(car_km - car_d_km)
    km_to_gas_remain = (gas_conmp*car_remain_km)/100

    return km_to_gas_remain
 




def pythagorean(x1, x2, y1 , y2):
    """
    Function for performing the calculations
    """
    delta_x = x1-x2
    delta_y = y1-y2

    # Calculate the length of the trip (m)
    m = sqrt(delta_x**2 + delta_y**2)

    return m
 


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
