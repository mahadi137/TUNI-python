"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def user_data(ask_pri_info):
    """Get user related primary data"""
    while True:
        user_input = int(input(ask_pri_info))

        if user_input >= 0:
            return user_input
        
def calculate_dose(pat_weight, passed_hr, total_doze_24):
    """calculation of parasetamol doze
    15mg per kg of total body weight"""

    if passed_hr >= 6 and total_doze_24 < 4000:
        more_dose = (4000 - total_doze_24)
        dose_per_weigth = pat_weight * 15
        if more_dose >= 0 and dose_per_weigth > more_dose:
            return more_dose
        else: return dose_per_weigth
    else: return 0
    


def main():
    pat_weight = user_data("Patient's weight (kg): ")
    passed_hr = user_data("How much time has passed from the previous dose (full hours): ")
    total_doze_24 = user_data("The total dose for the last 24 hours (mg): ")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)
    

    calcu_dose = calculate_dose(pat_weight, passed_hr, total_doze_24)
    print(f"The amount of Parasetamol to give to the patient: {calcu_dose}")


if __name__ == "__main__":
  main()
