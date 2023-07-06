# Mon10Jul.py

# 3.6.1.9 LAB - Operating with lists basic

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]        # list
temp_list = []                                  # temp list to store unique numbers

for number in my_list[:]:                       # for loop to iterate through numbers in my_list
    if number not in temp_list:                 # if number is not in the new list:
        temp_list.append(number)                # append the number to new_list
    else:
        continue                                # if it is in the new list, skip the append operation

my_list = temp_list                             # rename to original list

print(my_list)                                  # print list
