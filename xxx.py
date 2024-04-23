from math import sqrt
def pythagorean(x1, x2, y1 , y2):
    """
    Function for performing the calculations
    """
    delta_x = x1-x2
    delta_y = y1-y2

    # Calculate the length of the trip (m)
    m = sqrt(delta_x**2 + delta_y**2)

    return m

def km_to_gas_conv(car_km, car_d_km, gas_conmp):
    """
    calculate remaining car km capacity and convert
    km to gas.
    """
    car_remain_km = abs(car_km - car_d_km)
    km_to_gas_remain = (gas_conmp*car_remain_km)/100

    return km_to_gas_remain
 


def coordinates(x, y):
    """
    Implemented just to write less for clean code.
    """

    return x, y



def drive(prv_x, prv_y, new_x, new_y, gas, gas_consumption):
 
    
    car_curr_drive_capacity = (100/gas_consumption)*gas #100km can drive with 10 L gas, where car consumption is 10L per 100km
    print(car_curr_drive_capacity)   

    #actual unit for car drove
    car_drive = pythagorean(prv_x, new_x, prv_y , new_y)
    print(car_drive)
    
    if car_curr_drive_capacity < car_drive:
        car_can_not_go = car_drive - car_curr_drive_capacity
        print("car can not go", car_can_not_go)
        if prv_x == new_x:
            new_cor_y = car_curr_drive_capacity - abs(prv_y)
            reach_new_x, reach_new_y = coordinates(new_x,new_cor_y)

        if prv_y == new_y:
            new_cor_x = car_curr_drive_capacity - abs(prv_x)
            reach_new_x, reach_new_y = coordinates(new_cor_x,new_y)
        
        car_drove = car_curr_drive_capacity
        print("car_drove", car_drove)
        # all capacity taken till now
        gas_remain = km_to_gas_conv(car_curr_drive_capacity, car_drove, gas_consumption)
        

        return gas_remain, reach_new_x, reach_new_y
    
    else:
        
        if prv_x == new_x:
            new_cor_y = car_drive - abs(prv_y)
            reach_new_x, reach_new_y = coordinates(new_x,new_cor_y)

        if prv_y == new_y:
            new_cor_x = car_drive - abs(prv_x)
            reach_new_x, reach_new_y = coordinates(new_cor_x,new_y)
        
        car_drove = car_drive
        print("car_drove", car_drove)
        # all capacity taken till now
        gas_remain = km_to_gas_conv(car_curr_drive_capacity, car_drove, gas_consumption)


        return gas_remain, reach_new_x, reach_new_y
    
gas_remain, reach_new_x, reach_new_y = drive(-10, -60, -10, -10, 1, 10)
    


print(f"gas_remain: {gas_remain}, reach_new_x: {reach_new_x}, reach_new_y: {reach_new_y}")