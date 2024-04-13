def main():
    # Print information to the user.
    print ("Hello! I draw rectangles for you.")

    # The flag variable for the main loop.
    do_the_main_loop = True

    # Draw rectangles until the user ends the program.
    while do_the_main_loop:
        # Read the drawing character for the border and the character
        # that fills the rectangle.
        border_char = input("Please, enter the border character: ")
        fill_char = input("Please, enter the fill character: ")
        
        # Read the width and height and convert them to integers
        height_as_string = input("Please, enter the height: ")
        height = int(height_as_string)
        width_as_string = input("Please, enter the width: ")
        width = int(width_as_string)

        # A outer loop for printing one row on each iteration.
        for row_counter in range(1, height + 1):            
            # A inner loop for the printing of a single row.
            for column_counter in range(1, width + 1):
                # Print a border character. Do not end the line.
                if (row_counter == 1 or row_counter == height
                or column_counter == 1 or column_counter == width):
                    print(border_char, end = "")
                # Print the fill character. Do not end the line.
                else:
                    print(fill_char, end = "")
            
            # End the line so that the next row starts from
            # the beginning of the next row.
            print()
            
        # Determine whether the user wants to continue or stop drawing.
        choice = input("(c)continue or (q)uit? ")
        
        # Flip the flag, if the user wants to exit. Any other input
        # continues the program. If is not optimal, but better solution
        # cannot be done, because of the exercises.
        if choice == "q":
            do_the_main_loop = False

if __name__ == "__main__":
    main()