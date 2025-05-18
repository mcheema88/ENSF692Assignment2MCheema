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

    # This is setting up objects for my sensor and giving it the default values as instructed by the assignment
    # Essentially this will give it 3 field that we can update with inputs in the main code
    # The default conditions are going to be green, no and no. However input can change that
    # And then my plan is to use update status as my way to check and give a reccomendation
    def __init__(self):
        self.colour = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        self.currentStatus = "proceed"

    # Replace these comments with your function commenting
    def update_status(sensor): # You may decide how to implement the"arguments for this function
        currentStatus;
        if sensor.pedestrian or sensor.vehicle == "yes":
            currentStatus = "STOP"
        elif sensor.colour == "red"
            currentStatus = "STOP"
        elif sensor.colour == "yellow":
            currentStatus = "Caution"
        elif:
            currentStatus == "Proceed"



# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    pass


# Complete the main function below
def main():

    my_sensor = Sensor()


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
                my_sensor.colour = colour
                break
            else:
                print("Invalid vision change")

    if condition == 2 :
        acceptable_responses = ["yes", "no"]
        while True: 
            responses = input("What change has been identified: ");
            if responses_pedestrian in acceptable_responses:
                my_sensor.pedestrian = responses_pedestrian
                break
            else:
                print("Invalid vision change")

    if condition == 3 :
        acceptable_responses = ["yes", "no"]
        while True: 
            responses_vehicle = input("What change has been identified: ");
            if responses_vehicle in acceptable_responses:
                my_sensor.vehicle = responses_vehicle
                break
            else:
                print("Invalid vision change")

    if condition == 0:
        return

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
