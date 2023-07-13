# Mock_exam.py

# complete each task which is shown as a comment.
# complete each task directly below the comment
# each task shows a task number, and number of marks awarded
# on each task requiring an output, ensure the task goes on a separate line (unless stated)
# and ensure that it states the task number prior to any output e.g. Task 11
# upload your final file to your assigned folder share on class.net
# \\192.168.130.21\chshare\regiNumber

#####################################################
# Section 1 25 Marks here is a little test

# 1) Create and Assign a type float variable called fltOne the value 10 (3)
fltOne = float(10)

# 2) Create and Assign a type float variable called fltTwo the value 20 (3)
fltTwo = float(20)

# 3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)
fltThree = float(fltOne * fltTwo)

# 4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)
stringOne = "The product of fltOne and fltTwo ="

# 5) On the console, output stringOne and fltThree (in that order) (3)
print(stringOne, fltThree)

# 6) increment fltOne  (3)
fltOne += 1

# 7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". \
# Ensure a float is given (4)
fltTwo = float(input("Please provide another number for fltTwo: "))

# 8) on the console, output the product of fltOne and fltTwo with a suitable message (3)
fltThree = float(fltOne * fltTwo)
print(stringOne, fltThree)

#####################################################
# Section 2 35 Marks

# 8) take the input from fltTwo and apply a decision based on the number inputted .
# The decision should be based on if the user inputs a number below 100
# the code should output "below 100" (5)
if fltTwo < 100:
    print("below 100")

# 9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)
# Using if, else and elif, output the following:
# If the product is below 0, output "below 0"
# if the product is 0 output "value is zero"
# if the product is above 0 output "above 0" (8)
diff = fltOne - fltTwo
product = ""
if diff < 0:
    product = "below 0"
elif diff == 0:
    product = "value is zero"
else:
    product = "above 0"
print(product)

# 10) create a list called listOfInts (4)
ListOfInts1 = []

# 11 part a) create a for loop to iterate through the above list and populate the list with
# {4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)

# list comprehension
ListOfInts = [num for num in range(4,23,2)]
print(f"The contents of ListOfInts: \n{ListOfInts}")

# list append for loop
for num in range(4, 23, 2):
    ListOfInts1.append(num)
print(f"The contents of ListOfInts: \n{ListOfInts}")

# 11 part b) create a for loop to iterate through the above list and
# multiply each value by three assigning the new value to the respective
# index in the list. The list should now look like {12,18,24.....} (8)

temp_list = []
for item in ListOfInts:
    item *= 3
    temp_list.append(item)

ListOfInts = temp_list

# 11 part c )output listOfInts to the screen with a suitable message (3)

print(f"The new contents of ListOfInts where the values have multipled by 3: \n{ListOfInts}")

#####################################################
# Section 3 20 marks

# 14) create a function which calculates a decrease of a given percentage (10 marks)
# the function should be called calcPerc
# the function should take a cost parameter and a percentage parameter
# it should return the cost less the percentage amount
# For example if the paramenters are cost = 100 and percentage = 50, it should return 50.
# For another example, if the parameters are cost = 50 and percentage = 10, it should return 45.
# The percentage value should assume 10% if no value is given
def calcPerc(cost, percent=10):
    price = cost - (cost / 100 * percent)
    return int(price)

print(calcPerc(50, 20))

# 15) create a function called caseChanger which takes a string argument written all in lower case
# It will output all letters in lowercase except e which it will conver to capital E (10 marks)
# For example, caseChanger("hello") prints hEllo to the console
def caseChanger(input_string):
    if type(input_string) != str:
        return "Incorrect data type"

    word = ""
    for char in input_string:
        if char not in "eE":
            char = char.lower()
            word += char
        elif char in "eE":
            char = char.upper()
            word += char
        else:
            return None
    return word

print(caseChanger("HELLOOO BEEE"))

#####################################################
# Section 4 20 marks

# 16)a) Create a list that represents a set of students. The list should contain the following
# students: Clark,Horan,Rai,White,Cooper,Jones,Cox,Smith (4 marks)

students = ["Clark", "Horan", "Rai", "White", "Cooper", "Jones", "Cox", "Smith"]

# b) use a method to order the students so that they are in alphabetical order (3 marks)

students.sort()
print(students)

# 17) create a tuple that represents exam marks with the following data. (4 marks)
# These are the respective exam marks for the alphabetically ordered student list
# 65,66,67,80,90,65,65,93
marks = (65, 66, 67, 80, 90, 65, 65, 93)


# 18) Dictionary question (9 marks)
# create a dictionary which joins the student with their corresponding mark.
# There is a manual way of doing this or a way involving using the previous tuple and list
# you will be awarded highest marks for
# output the student with their corresponding mark

student_marks = {}
counter = 0
for name in students:
    student_marks[name] = marks[counter]
    counter += 1
print(student_marks)

# theory tester
x = 2
y = 3
z = 4
print(x+y+z)
# 9

z = y = x = 1
print(x,y,z, sep='!')
# 1!1!1

x = 2
y = 3
x = x == y
print(x)
# False

for i in range(2):
	print("#")
else:
	print("#")
# ###

z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)
# True

vals = [3,2,1,0]
vals[0],vals[1],vals[2],vals[3] = vals[3],vals[2],vals[1],vals[0]
print("8",vals)
# 8 [0,1,2,3]


tup = (1,2,4,8)
tup = tup[-3:-1]
tup = tup [1]
print(tup)
# 4

def fun(x):
    global y
    y = x ** x
    return y

fun(3)
print(y)
# 27
