# Fri Test

# 2.6.1.9 LAB
print("*** Simple input & output LAB - Input 2 numbers to perform some basic arithmatic ***")
# user inputs two numerical values
lst=[]                                                              # create empty list for user inputs

var = True                                                          # variable to control while loop
while var == True:                                                  # enter while loop
    try:                                                            # try condition
        input1 = float(input("Enter the first number : "))          # receive user input and try to convert to float
        lst.append(input1)                                          # if successful append input to lst
        var = False                                                 # if successful var changed to false and loop broken
    except ValueError:
        print("None numerical input detected. Please try again...") # if TypeError detected, print and loop

var = True                                                          # as above ^
while var == True:
    try:
        input2 = float(input("Enter the second number : "))
        lst.append(input2)
        var = False
    except ValueError:
        print("None numerical input detected. Please try again...")

# arithmatic
addition = lst[0] + lst[1]          # call from lst from position 0 and position 1 and carry out arithmatic
subtraction = lst[0] - lst[1]
multiplication = lst[0] * lst[1]
division = lst[0] / lst[1]
exponent = lst[0] ** lst[1]
floordiv = lst[0] // lst[1]

# print arithmatic results
print(f'The result of {lst[0]} + {lst[1]} is equal to {addition}')
print(f'The result of {lst[0]} - {lst[1]} is equal to {subtraction}')
print(f'The result of {lst[0]} * {lst[1]} is equal to {multiplication}')
print(f'The result of {lst[0]} / {lst[1]} is equal to {division}')
print(f'The result of {lst[0]} ** {lst[1]} is equal to {exponent}')
print(f'The result of {lst[0]} // {lst[1]} is equal to {floordiv}')

print("\nThat's all, folks!\n")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


# 2.6.1.10 LAB
print("*** Operators and expressions LAB1 - Input a number to evaluate against a confusing expression ***")
# user input assigned to x as a float
var = True
while var == True:
    try:
        x = float(input("Enter value for x: "))
        var = False
    except ValueError:
        print("None numerical input detected. Please try again...")

# expression arithmatic
y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

# print end value of y where x is equal to user input
print(f"\n y = {y} where x is equal to {x}.")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


# 2.6.1.11 LAB
print("*** Operators and expressions LAB2 - Evaluate the end time of a period of time ***")
# input variables for time calculation with exception handling
var = True                                                              # variable to control the loop
while var == True:                                                      # enter while loop
    try:                                                                # try condition
        hour = int(input("Starting time (hours): "))                    # user input to hour variable
        if hour > 23 or hour < 0:                                      # if statement to catch input over 23 hours
            print("Hour(s) to range between 0 - 23")                    # print instruction to user
            var = True                                                  # set var to True staying in loop
        else:                                                           # else statement
            var = False                                                 # set var to false to break loop
    except ValueError:
        print("None numerical input detected. Please try again...")     # if TypeError detected, print and loop
        var = True

var = True
while var == True:
    try:
        mins = int(input("Starting time (minutes): "))
        if mins > 59 or mins < 0:
            print("Minute(s) range between 0-59")
            var = True
        else:
            var = False
    except ValueError:
        print("None numerical input detected. Please try again...")

var = True
while var == True:
    try:
        dura = int(input("Event duration (minutes): "))
        var = False
    except ValueError:
        print("None numerical input detected. Please try again...")

total_mins = mins + dura                # calculate total amount of minutes
hour = hour + (total_mins // 60)        # add additional hours from minutes input larger than 60
total_mins = total_mins % 60            # modulo minutes to return result between 0-60
hour = int(hour % 24)                   # modulo hours to return result between 0-24

print(f"\nThe total time duration is: {hour}:{total_mins}")          # int result
