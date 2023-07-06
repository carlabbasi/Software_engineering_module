# Fri7Jul.py

import time

# 3.4.1.6 LAB - Basics of lists

print("\nThere once was a hat. That contained no rabbit, but a list of five numbers:\n")

hat_list = [1, 2, 3, 4, 5]                      # create list and add values
print(f"Hat list: {hat_list}")

user_input = (int(input("Enter an integer number: ")))  # prompt user to add value
hat_list[2] = user_input                                # replace list index [2] with user input
print(f"Hat list updated with user input: {hat_list}")

del hat_list[-1]                                # delete last item in list
print(f"Hat list with last entry removed: {hat_list}")

print(f"Hat list current length is: {len(hat_list)}")   # print length of hat list
print(f"Final hat list: {hat_list}")            # print list
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.4.1.13 LAB - the BEATLES

beatles = []                                    # create empty list
print("Step 1:", beatles)

beatles.append("John Lennon")                   # append name
beatles.append("PaulMcCartney")                 # append name
beatles.append("George Harrison")               # append name
print("Step 2:", beatles)

for names in range(1):                          # for loop to add 2 names to list
    while True:
        if "Stu Sutcliffe" not in beatles:      # while loop to make sure name spelt correctly
            input1 = input("Type \"Stu Sutcliffe\" to add to beatles list: ")
            if input1 != "Stu Sutcliffe":
                continue
            else:
                beatles.append(input1)          # if input correct append to list
                break
    while True:
        if "Pete Best" not in beatles:          # while loop to make sure name spelt correctly
            input1 = input("Type \"Pete Best\" to add to beatles list: ")
            if input1 != "Pete Best":
                continue
            else:
                beatles.append(input1)          # if input correct append to list
                break
    break                                       # break for loop
                                    # break for loop
print("Step 3:", beatles)
time.sleep(0.5)

for name in range(2):                           # for loops to delete last list entry (repeats twice)
    del(beatles[-1])
print("Step 4:", beatles)
time.sleep(0.5)

beatles.insert(0, "Ringo Star")                 # insert into list at index 0 (first)
print("Step 5:", beatles)
time.sleep(0.5)

# testing list length                            # print list length
print("The Fab", len(beatles))
