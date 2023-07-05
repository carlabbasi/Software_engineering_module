# Fri7Jul.py

# 3.4.1.6 LAB - Basics of lists

hat_list = [1, 2, 3, 4, 5]                      # crate list and add values
user_input = (int(input("Enter an integer number: ")))  # prompt user to add value
hat_list[2] = user_input                        # replace list index [2] with user input
del hat_list[-1]                                # delete last item in list
print(len(hat_list))                            # print length of hat list
print(hat_list)                                 # print list


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
print("Step 3:", beatles)

for name in range(2):                           # for loops to delete last list entry (repeats twice)
    del(beatles[-1])
print("Step 4:", beatles)

beatles.insert(0, "Ringo Star")                 # insert into list at index 0 (first)
print("Step 5:", beatles)

# testing list legth                            # print list length
print("The Fab", len(beatles))
