#MonTest


# 3.1.1.4 LAB - two line code to evaulate if n is more than or equal to 100
n = int(input("Enter number: "))
print(n >= 100)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.1.1.10 LAB - plant checker
plant = input("Enter a plant name: ")

if plant == "Spathiphyllum": print("Yes - Spathiphyllum is the best plant ever!")	# if spelt upper case S
elif plant == "spathiphyllum": print("No, I want a BIG Spathiphyllum!")				# and if spelt lower case s
else: print(f"Spathiphyllum! Not {plant} !")										# if other plant

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.1.1.11 LAB - Tax calculator
# inputs
income = float(input("Enter the annual income: "))              # user enters income
jury = input("Did you do jury duty this year? Enter y/n? ")     # user declares jury status

# tax calculation
if income < 85528:
	tax = (income * 0.18) - 556.02                              # calculation for tax on lower income
else:
	tax = ((income - 85528) * 0.32) + 14839.02                  # calculation for tax on higher income

# jury calculation
if jury == "y": tax = tax / 2                                   # Divide tax by two if y inputted
elif jury == "Y": tax = tax / 2                                 # Divide tax by two if Y inputted

if tax < 0.0: tax = 0.0

tax = round(tax, 0)
print(f"The tax is: {tax} thalers")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.1.1.12 LAB - Leap year checker
# input
year = int(input("Enter a year: "))                                 # user inputs year

# year calculation
if year < 1582:                                                     # is year before 1582?
	print(f"{year} is before the start of the Gregorian calendar")
else:
	if year % 4 != 0:                                               # is year dividable by 4?
		print(f"{year} is a common year")
	elif year % 100 != 0:                                           # is year dividable by 100?
		print(f"{year} is a leap year")
	elif year % 400 != 0:                                           # is year dividable by 400?
		print(f"{year} is a common year")
	else:                                                           # otherwise leap year.
		print(f"{year} is a leap year")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
