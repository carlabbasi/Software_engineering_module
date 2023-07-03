# 3.1.1.12 Year calculator
year = int(input("Enter a year: "))                     # enter year

if year < 1582:                                         # year before 1582?
    print("Year is before the start of the Gregorian calendar")

elif year % 4 != 0:                                     # year divisible by 4?
    print(f"{year} is a common year.")

elif year % 100 !=0:                                    # year divisible by 100?
    print(f"{year} is a leap year.")

elif year % 400 !=0:
    print(f"{year} is a common year.")                  # year divisible by 400?

else:
    print(f"{year} is a leap year.")                    # else = leap year
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
