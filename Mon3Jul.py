# Mon3Jul.py


# 3.1.1.4 LAB - two line code to evaulate if n is more than or equal to 100
n = int(input("Enter number: "))
print(n >= 100)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.1.1.10 LAB - plant checker
plant = input("Enter a plant name: ")

if plant == "Spathiphyllum": print("Yes - Spathiphyllum is the best plant ever!")	# if spelt upper case S
elif plant == "spathiphyllum": print("No, I want a BIG Spathiphyllum!")			# and if spelt lower case s
else: print(f"Spathiphyllum! Not {plant} !")						# if other plant

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 3.1.1.11 LAB - Tax calculator
# inputs
income = float(input("Enter the annual income: "))              # user enters income
jury = input("Did you do jury duty this year? Enter y/n? ")     # user declares jury status

# tax calculation
if income < 85528: tax = (income * 0.18) - 556.02               # calculation for tax on lower income
else: tax = ((income - 85528) * 0.32) + 14839.02                # calculation for tax on higher income

# jury calculation
if jury == "y" or jury == "Y": tax = tax / 2                    # Divide tax by two if y/Y inputted

if tax < 0.0: tax = 0.0

tax = round(tax, 0)						# round tax
print(f"The tax is: {tax} thalers")				# print tax

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

