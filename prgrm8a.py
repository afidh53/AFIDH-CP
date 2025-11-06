import calendar
year=int(input("enter year:"))
leap_year=calendar.isleap(year)
if leap_year:
    print("The year is leap year")
else:
    print("The year is non leap year")
    