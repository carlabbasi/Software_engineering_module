# Thur29Jun.py

print("2.4.1.7 LAB \n")
# create variables with value == number of apples
john = 3
mary = 5
adam = 6

# print variables on one line, separated by commas
print(john, mary, adam, sep=", ")

# new variable equal to addition of three previous variables
total_apples = john + mary + adam

# print new variable to console
print("Total apples =", total_apples)

# new variable to average the amount of apples
names = john + mary + adam
vars = 3
average_apples = names / vars
average_apples_floor = names // vars

# print average variables to console
print("Average apples =", average_apples)
print("Average apples (rounded) =", round(average_apples, 2))
print("Average apples (floor divised) =", average_apples_floor)
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


print("2.4.1.9 LAB \n")
# distance variables
kilometers = 12.25
miles = 7.38

# conversion values
one_mile_in_km = 1.609344
one_mile_in_furlong = 8
one_kilometer_in_furlong = 4.979695379

# conversion arithmatic
miles_to_kilometers = miles * one_mile_in_km
kilometers_to_miles = kilometers / one_mile_in_km
miles_to_furlongs = miles * one_mile_in_furlong
kilometers_to_furlongs = kilometers * one_kilometer_in_furlong

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers", "or", round(miles_to_furlongs, 2), "furlongs.")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles", "or", round(kilometers_to_furlongs, 2), "furlongs.")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


print("2.4.1.10 LAB \n")
# Declare variable and convert to float
x = 1
x = float(x)

# Evaluate expression 3x**3 - 2x**2 + 3x - 1 and assign to y variable
print("Evaluate 3x**3 - 2x**2 + 3x - 1 \n")
y = (3 * (x ** 3) - 2 * (x ** 2) + (3 * x) - 1)

# print result
print("y =", y, "where x =", x)
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


print("2.4.1.11 SUMMARY \n")
print("Ex1 = 3")
print("Ex2 = 101, m 101, del")
print("Ex3 = 11")
print("Ex4 = Shortcuts (!) \n")


a = 6
b = 3
a /= 2 * b
print( "a /= 2 *b =", a)

a = 6
b = 3
a = a / 2 * b
print("a = a / 2 * b =", a)
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


print("2.5.1.2 LAB \n")
#this program computes the number of seconds in a given number of hours
#this program has been written two days ago <-- Remove!

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) # printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours <--Removed # from beginning


#here we should also print "Goodbye", but a programmer didn't have time to write any code <-- Remove!
print("Goodbye!") # Added goodbye
#this is the end of the program that computes the number of seconds in 3 hour <-- Remove!
