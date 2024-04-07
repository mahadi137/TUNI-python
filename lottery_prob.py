"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def read_integer(prompt):
    """Read user inputs.

    :param prompt: string, text to ask for total number of ball.
    :return: .
    """

    user_input = int(input(prompt))

    return user_input



def read_inputs():
    """Read user inputs by read_integer function.

    :param : nothing
    :return: int
    """

    total_ball = read_integer("Enter the total number of lottery balls: ")
    total_drawn_ball = read_integer("Enter the number of the drawn balls: ")

    return total_ball, total_drawn_ball

    


def get_probability(number):
    """Loop through number for probality.

    :param number: int
    :return: int
    """

    result = 1

    #loop through and multiply
    for ball in range(1, number + 1):
        result *= ball
    
    return result



def probability_calcu(total_ball, total_drawn_ball):
    """Calculates probability of wining. Standard rule for calculation is a!/(a-p)!.p!
    a is total ball, p is total drawn ball

    :param total_ball, total_drawn_ball: int. all are positive integer
    :return: int
    """
    
    #(a-p)!
    substract = total_ball - total_drawn_ball

    substract_prob = get_probability(substract)
    t_ball_prob = get_probability(total_ball)
    draw_ball_prob = get_probability(total_drawn_ball)

    #Calculation of probability
    #formula: a!/(a-p)!.p!
    probability = int(t_ball_prob / (substract_prob * draw_ball_prob))
        
    print(f"The probability of guessing all {total_drawn_ball} balls correctly is 1/{probability}")
    




def main():
    #get total lottery balls
    total_ball, total_drawn_ball = read_inputs()
    
    if total_ball < 0: 
        print("The number of balls must be a positive number.")
    elif total_ball < total_drawn_ball:
        print("At most the total number of balls can be drawn.")
    else:
        #probability calculation
        probability_calcu(total_ball, total_drawn_ball)
    
    
    

   
    

    



if __name__ == "__main__":
    main()

