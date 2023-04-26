# Dela Cruz, Lailanie E. _ BSCpE 1-4
# Assignment 4
# Programming Exercises 3

# Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n

def multiple_line():
    # Create text file named mylife.txt
    with open('mylife.txt', 'a') as multiple_line:
        while True:
            # Ask the user to enter a line of text
            line = input("Enter line: ")
            # Write the entered line to the file
            multiple_line.write(f'Enter line: {line}\n')

            # Ask the user if there are more lines to be added
            while True:
                more_lines = input("Are there more lines y/n? ")
                if more_lines.lower() in ['y', 'n']:
                    # Write the entered line to the file
                    multiple_line.write(f'Are there more lines y/n? {more_lines}\n')
                    break
                # If the user enters inalid key, print out 'Invalid input'
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            # If the user enters 'n', break out of the process
            if more_lines.lower() == 'n':
                break            
            # If the user enters 'y', continue the process
            else:
                continue
            
multiple_line()
