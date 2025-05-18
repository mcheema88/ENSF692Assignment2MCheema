# input_processing.py
# Marley Cheema, ENSF 692 Spring 2025 - Sarah Shah


# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.

#MARLEY CHEEMA


# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        pass

    # Replace these comments with your function commenting
    def update_status(): # You may decide how to implement the"arguments for this function
        pass



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass

ssdddd

# Complete the main function below
def main():

    potential_inputs = [1,2,3,0];



    print("Are Changes are detected for vision input?")
    
    while True: 
        condition = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "));
        if condition in potential_inputs:
            break
        else:
            print("You must select either 1, 2, 3 or 0.")


    if condition == 1 :
        acceptable_colours = ["green", "yellow", "red"]
        while True: 
            colour = input("What change has been identified: ");
            if colour in acceptable_colours:
                break
            else:
                print("Invalid vision change")

    if condition == 2 :
        acceptable_responses = ["yes", "no"]
        while True: 
            responses = input("What change has been identified: ");
            if responses in acceptable_responses:
                break
            else:
                print("Invalid vision change")

    if condition == 3 :
        acceptable_responses = ["yes", "no"]
        while True: 
            responses = input("What change has been identified: ");
            if responses in acceptable_responses:
                break
            else:
                print("Invalid vision change")



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

