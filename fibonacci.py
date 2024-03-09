"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():
    ask_number = int (input ("How many Fibonacci numbers do you want? "))
    sequence = 1
    fib_list = [0, 1]

    while sequence < ask_number:
        fib_num = fib_list [-1] + fib_list [-2]
        fib_list.append (fib_num)

        sequence += 1

    for i in range (1, len (fib_list)):
        print (f"{i}.", fib_list [i])
        


if __name__ == "__main__":
    main()
