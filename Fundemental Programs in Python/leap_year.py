#Leap Year Program in Python

def leap_year(year):
    if year % 400 == 0:
        print('leap year')
    elif year % 4 == 0:
        print('leap year')
    elif year % 100 == 0:
        print('not a leap year')
    else:
        print('not a leap year')

leap_year(2001)