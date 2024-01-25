
year = int(input("Year: "))
month = int(input("Month: "))

def leap_year(year):
    if year % 4 == 0:
        return True
        if year % 100 == 0:
            return True
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def days_in_month(year, month):
    if leap_year(year) == True:
        print(f"{year} is a leap year")
        if month == 2:
            print("29 days")
        elif month == 1 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12:
            print("31 days")
        else:
            print("30 days")
    else:
        print(f"{year} is not a leap year")
        if month == 2:
            print("28 days")
        elif month == 1 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12:
            print("31 days ")
        else:
            print("30 days")


days_in_month(year, month)