# Fri7Jul.py

# 3.4.1.6 LAB - Basics of lists

hat_list = [1, 2, 3, 4, 5]

user_input = (int(input("Enter an integer number: ")))

hat_list[2] = user_input

del hat_list[-1]

print(len(hat_list))

print(hat_list)


# 3.4.1.13 LAB - the BEATLES

beatles = []
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("PaulMcCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for names in range(2):
    if "Stu Sutcliffe" not in beatles:
        input1 = input("Type \"Stu Sutcliffe\" to add to beatles list: ")
        if input1 != "Stu Sutcliffe":
            continue
        else:
            beatles.append(input1)

    if "Pete Best" not in beatles:
        input2 = input("Type \"Pete Best\" to add to beatles list: ")
        if input2 != "Pete Best":
            continue
        else:
            beatles.append(input2)
print("Step 3:", beatles)

del(beatles[-1])
del(beatles[-1])
print("Step 4:", beatles)

beatles.insert(0, "Ringo Star")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
