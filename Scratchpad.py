
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


def test1():
    test_data = [1900, 2000, 2016, 1987]        # test loop
    test_results = [False, True, True, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "->", end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")


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
    if is_year_leap1(year) and month == 2:
        return 29
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28


def test2():
    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")


test1()
test2()
