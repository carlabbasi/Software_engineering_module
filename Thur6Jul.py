# Thur6Jul.py

import time                      # import time for use of sleep function

# 3.2.1.14 - Essentials of the while loop

# intro "animation"
print("                      ^ ")
time.sleep(0.1)
print("                    /   \\")
time.sleep(0.1)
print("                  /       \\        \\---- The pyramid layer")
time.sleep(0.15)
print("                /           \\        \\ ---- TURBO calculator")
time.sleep(0.15)
print("              /               \\")
time.sleep(0.2)
print("            /        __        \\")
time.sleep(0.2)
print("          /_________|  |_________\\")
time.sleep(0.25)
print("                    /  /")
time.sleep(0.25)
print("                   /  /")

user = "Y"                          # set user variable to Y for application control
while user == "Y":

    total_blocks = 0                # variable initially defined in case try statement fails

    try:                            # create exception to avoid value error if a string is input
        total_blocks = int(input("\nEnter the total amount of blocks to calculate the amount of layers for a pyramid: "))
                                    # user enters total amount of blocks
    except ValueError:
        print("\nCalculator only works with positive integer numbers (no strings)")
        continue                    # continue loop if error detected
    except KeyboardInterrupt:                           # error handling for keyboard interrupt
        user = "N"
        continue

    blocks = total_blocks           # second variable created to preserve users input
    counter = 1                     # create a counter to increment blocks per layer by 1 per loop
    height = 0                      # create a counter to increment height by 1 layer per loop

    if total_blocks == 0:
        print("\nCalculator does not work with 0 value")
        continue

    if "-" in str(blocks):          # check input to avoid any negative numbers
        print("\nCalculator only works with positive integer numbers (no negative numbers)")
        continue                    # continue loop if negative number detected

    while blocks != 0:              # while loop entered as long a blocks is not equal 0
        blocks -= counter           # blocks - counter value
        counter += 1                # counter incremented by 1 as each additional layer requires 1 additional block
        height += 1                 # height incremented by 1 per loop to add a "layer"
        if blocks < counter:        # counter will always count blocks required for the next full layer
            break                   # if blocks is lower than counter, loop breaks

    # when loop is broken, prints how many blocks were initially entered from the 'total_blocks' variable, how many-
    # full layers were achieved in the 'height' variable and how many blocks are remaining in the 'blocks' variable
    print(f"""
    With {total_blocks} blocks you can build a pyramid with {height} layer(s).
    You will have {blocks} blocks left over.
    """)
    try:
        user = (input("Press Y to try another number, anything else to quit: "))     # added additional while loop to-
        user = user.upper()                         # run loop again for multiple number entries for ease of testing.
    except KeyboardInterrupt:                       # error handling for keyboard interrupt
        user = "N"
        continue

print("\n*** Application terminated ***")           # application terminates if user inputs anything other than 'Y'.
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.2.1.15 - Collatz's hypothesis
print("*** Collatz's hypothesis ***")

user = "Y"                                  # set user variable to Y for application control
while user == "Y":                          # while loop for application control
    c0_numbers = []                         # create empty list to store each number that c0 becomes during calculation

    try:                                    # create exception to avoid value error if a string is input
        c0 = int(input("\nEnter a value to run against Collatz's hypothesis: "))        # user enters a value

    except ValueError:
        print("\nValue must be non-negative non-zero integer number!")  # message if Value Error detected
        continue
    except KeyboardInterrupt:               # error handling for keyboard interrupt
        user = "N"
        continue

    if c0 == 0:                             # if statement to check if c0 is == 0
        print("\nValue must be non-zero integer number!")
        continue

    if "-" in str(c0):                      # if statement to check if c0 is a negative number
        print("\nValue must be non-negative integer number!")
        continue

    steps = 0                               # steps variable to count total amount of steps to get c0 to a value of 1

    while c0 != 1:                          # while loop which stops when c0 == 1
        if c0 % 2 == 0:                     # check if c0 is even
            c0 /= 2                         # if even divide c0 by 2
            steps += 1                      # steps count incremented
            c0_numbers.append(int(c0))      # append current c0 value to c0_numbers list

        else:                               # if c0 not even
            c0 = (c0 * 3) + 1               # c0 multiplied by 3 plus 1
            steps += 1                      # steps count incremented
            c0_numbers.append(int(c0))      # append current c0 value to c0_numbers list

    print(f"\n{c0_numbers}")                # once c0 == 1, print c0_numbers list containing all previous c0 values
    print(f"Total steps taken = {steps}")   # print steps variable containing count of steps taken to get to 1

    try:                                    # ask if the user wnats to try another number
        user = input("\nPress Y to try another number, anything else to quit: ") # if Y inputted, application control-
        user = user.upper()                                                     # while loop restarts
    except KeyboardInterrupt:               # error handling for keyboard interrupt
        user = "N"
        continue

print("\nApplication terminated")           # application termination message

