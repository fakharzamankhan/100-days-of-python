def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(y, m):
    if m>12 or m<1:
        return "Please enter a valid month"
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(y) and m==2:
        return 29
    return month_days[m-1]


year = int(input("Enter your year: "))
month = int(input("Enter your month: "))
days=days_in_month(year, month)
print(f"There is {days} days in {month} month of {year}.")

