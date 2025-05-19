# Marley Cheema, ENSF 692 Spring 2025 - Sarah Shah

#MARLEY CHEEMA

#Really enjoyed this assignment, took me a while to figure out how to structure, but once I started coding things started coming to me
# I liked using classes, at first I didnt read the README1.md file completely so I didnt know I had to use classes
# but once I figured out, I have come to the realization that save having to write so much code in main()
# which is awesome and keeps the code cleaner, and also helps makes storing of variables clear

#Had some problmes with syntax and error which took a while, I used chatgpt for some light troubleshooting(no code generation)
# which was super helpful and I will reference!

# This class is base of the code, and is used for initialization, setting fields and tracking inputs
#originally I thought I only need 3 fields -> colour, pedestrian and vehicle but over time I realized that to
# truly eliminate global variables, conditions could also just be moved within this class and be held and used to compare 
# in the main code

class Sensor:

    # This is setting up objects for my sensor and giving it the default values as instructed by the assignment
    # Essentially this will give it 3 field that we can update with inputs in the main code
    # The default conditions are going to be green, no and no. However input can change that
     
    # I ended up add 4 fields in this initialization (currentstatus which can also be modified and then 3 input conditions that
    # will be unchanged)
    def __init__(self):
        self.colour = "green"
        self.pedestrian = "no"
        self.vehicle = "no"
        self.currentStatus = 1
        self.potential_inputs = [1,2,3,0]
        self.acceptable_colours = ["green", "yellow", "red"]
        self.acceptable_responses = ["yes", "no"]



    # This function is key, an determines whether you should proceed or not
    # it takes self, so the object at had and evaluates whether or not the inputs that main prompts for changes the conditions
    # ot a combination of proceed, caution or stop
    # For context a 3 value in the field of currentStatus within the Sensor Class means stop, 2 means caution and 1 is proceed (also the default condition)
    def update_status(self): # You may decide how to implement the"arguments for this function
        if self.pedestrian == "yes" or self.vehicle == "yes":
            self.currentStatus = 3
        elif self.colour == "red":
            self.currentStatus = 3
        elif self.colour == "yellow":
            self.currentStatus = 2
        else:
            self.currentStatus = 1



# The sensor object should be passed to this function to print the action message and current status
# Based on the assignment requirements, I set this up as such so that this is a seperate function that takes the object I create of sensor
# and will execute print statements based on the currentStatus field, and the value the currently is occupied within it!!
# This is written with if and elif statements and values correspond to what I said above with 1, 2 & 3 within currentStatus
def print_message(sensor):
    if sensor.currentStatus == 1:
        print("\n")
        print("Proceed")
        print("\n")
        print("Light = " + sensor.colour + " , Pedestrian = " + sensor.pedestrian + " , Vehicle = " + sensor.vehicle + " .")
        print("\n")
    elif sensor.currentStatus == 2:
        print("\n")
        print("Caution")
        print("\n")
        print("Light = " + sensor.colour + " , Pedestrian = " + sensor.pedestrian + " , Vehicle = " + sensor.vehicle + " .")
        print("\n")
    elif sensor.currentStatus == 3:
        print("\n")
        print("STOP")
        print("\n")
        print("Light = " + sensor.colour + " , Pedestrian = " + sensor.pedestrian + " , Vehicle = " + sensor.vehicle + " .")
        print("\n")

# Complete the main function below
def main():

    #Creating the initial object of my_sensor from the class -> it will assume the default fields as defined above
    # but can be modified through user input
    my_sensor = Sensor()

    #potential_inputs = [1,2,3,0]; -> originally had this variable but it was removed and add to the class as a field so it is commented out
    
    # Huge while loop that keeps the program running and allows it to remember changed values - > not just default as required
    # only way to exit loop is through an input of 0 to end program
    while True:    
        
        print("Are Changes are detected for vision input?")
    
        # first loop within the main loop,
        # this is all about following the right logic path based on the user input
        # as a check it will keep running until a valid input is put in 
        while True: 
            condition = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "));
            #this ensures the condition value (user input) is right so that it can move through the program
            if condition in my_sensor.potential_inputs:
                break
            else:
                print("You must select either 1, 2, 3 or 0.")

        # First layer -> if user input is 1, we will move to changing the lights
        if condition == 1 :
            while True: 
                # allows a value to be inputted, because in while loop if it is not of the right format (apart of my_sensor.acceptable_colours), the loop will continue to prompt
                colour = input("What change has been identified: ");
                if colour in my_sensor.acceptable_colours: #ensuring that input is good
                    my_sensor.colour = colour # this is key -> modifying the field within the sensor object, so evaluation can occur
                    my_sensor.update_status() #using my update function that was created in the class to check based on the field updates if you should proceed, caution or stop.
                    print_message(my_sensor) # no based on sensor update printing out the corresponding result as requested.
                    break
                else:
                    print("Invalid vision change")



        #Identical logic as above just for these 2 conditions (an entry of 2 or 3) which deal with vehicle and pedestrian
        #Additionally have corresponding names and fields
        # however the updates_status() function apart of the class is the same, along with print_message() and are used the same, just looking
        # at slightly different fields
    
        if condition == 2 :
            #acceptable_responses = ["yes", "no"]
            while True: 
                responses_pedestrian = input("What change has been identified: ");
                if responses_pedestrian in my_sensor.acceptable_responses:
                    my_sensor.pedestrian = responses_pedestrian
                    my_sensor.update_status()
                    print_message(my_sensor)
                    break
                else:
                    print("Invalid vision change")

        if condition == 3 :
            #acceptable_responses = ["yes", "no"]
            while True: 
                responses_vehicle = input("What change has been identified: ");
                if responses_vehicle in my_sensor.acceptable_responses:
                    my_sensor.vehicle = responses_vehicle
                    my_sensor.update_status()
                    print_message(my_sensor)
                    break
                else:
                    print("Invalid vision change")

        if condition == 0:
            return



# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()
