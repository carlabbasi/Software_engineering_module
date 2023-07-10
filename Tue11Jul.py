
# 4.3.1.6 LAB - Leap year function
def is_year_leap(year):
    if year < 1582:                     # is year before 1582?
        return None
    else:
        if year % 4 != 0:               # is year dividable by 4?
            return False
        elif year % 100 != 0:           # is year dividable by 100?
            return True
        elif year % 400 != 0:           # is year dividable by 400?
            return False
        else:                           # otherwise leap year.
            return True


def test1():                                    # test loop
    test_data = [1900, 2000, 2016, 1987]        # test data
    test_results = [False, True, True, False]   # correct test result to check against
    print(f"Testing function is_leap_year with input data:\n {test_data}\n")
    for i in range(len(test_data)):             # for loop range, length == test data list
        yr = test_data[i]                       # i iterates through test data list to become yr vraiable
        print(yr, "->", end="")                 # yr printed with arrow
        result = is_year_leap(yr)               # yr is checked against is_leap_year function
        if result == test_results[i]:           # if result is same as test_result list: print OK, else failed
            print("OK")
        else:
            print("Failed")


test1()
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 4.3.1.7 LAB - Leap year days function
def is_year_leap1(year):
    if year < 1582:                     # is year before 1582?
        return None
    else:
        if year % 4 != 0:               # is year dividable by 4 = common
            return False
        elif year % 100 != 0:           # is year dividable by 100 = leap
            return True
        elif year % 400 != 0:           # is year dividable by 400 = common
            return False
        else:                           # otherwise leap year = leap
            return True


def days_in_month(year, month):
    if is_year_leap1(year) and month == 2:      # if year returns True from is_year_leap1 function and month is 2
        return 29                               # return 29 days for a leap year February
    elif month in [1, 3, 5, 7, 8, 10, 12]:      # else if month has 31 days, return 31
        return 31
    elif month in [4, 6, 9, 11]:                # elif month has 30 days, return 30
        return 30
    else:                                       # else return 28 for a normal february
        return 28


def test2():                                    # test loop
    test_years = [1900, 2000, 2016, 1987]       # test data years
    test_months = [2, 2, 1, 11]                 # test data months
    test_results = [28, 29, 31, 30]             # correct test results to check against
    print(f"Testing function days_in_month with input data:\n Years: {test_years}, Months: {test_months}\n")
    for i in range(len(test_years)):            # for loop range, length == test_years
        yr = test_years[i]                      # i iterates through test_years to become yr variable
        mo = test_months[i]                     # i iterates through test_months to become mo variable
        print(yr, mo, "->", end="")             # test data printed with arrow
        result = days_in_month(yr, mo)          # result checks against what is returned from days_in_month func
        if result == test_results[i]:           # if result is same as test_results, print OK, else print failed
            print("OK")
        else:
            print("Failed")


test2()
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# 4.3.1.8 LAB - Day of the year function
def is_year_leap(year):
    if year < 1582:                     # is year before 1582?
        return False
    else:
        if year % 4 != 0:               # is year dividable by 4 = common
            return False
        elif year % 100 != 0:           # is year dividable by 100 = leap
            return True
        elif year % 400 != 0:           # is year dividable by 400 = common
            return False
        else:                           # otherwise leap year = leap
            return True


def day_of_year(year, month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0

    if is_year_leap(year):
        month_days[1] = 29

    for i in range(month - 1):
        days += month_days[i]

    total_days = days + day
    return total_days

def test3():                                    # test loop
    test_years = [1900, 2000, 2016, 1987]       # test data years
    test_months = [2, 2, 1, 11]                 # test data months
    test_days = [28, 29, 23, 15]
    test_results = [59, 60, 23, 319]             # correct test results to check against
    print(f"Testing function days_of_year with input data:\n Years: {test_years}, Months: {test_months}, Days: {test_days}\n")
    for i in range(len(test_years)):            # for loop range, length == test_years
        yr = test_years[i]                      # i iterates through test_years to become yr variable
        mo = test_months[i]                     # i iterates through test_months to become mo variable
        day = test_days[i]
        print(yr, mo, day, "->", end="")             # test data printed with arrow
        result = day_of_year(yr, mo, day)          # result checks against what is returned from days_in_month func
        if result == test_results[i]:           # if result is same as test_results, print OK, else print failed
            print("OK")
        else:
            print("Failed")

test3()
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
