def is_year_leap(year):
    if year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


def days_in_month(year, month):
    days_in_month = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = days_in_month[month]
    if is_year_leap(year) and month == 2:
        days += 1
    return days


def day_of_the_year(year, month, day):
    pass


test_data = [1900, 2000, 2016, 1987, 23]
test_months = [2, 2, 1, 11, 12]
test_days = [41, 29, 13, 16, 55]
test_results = []

for i in range(len(test_data)):
    yr = test_data[i]
    mo = test_months[i]
    day = test_days[i]
    print(yr, mo, day, "->", end="")
    result = day_of_the_year(yr, mo, day)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
