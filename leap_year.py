year = 2025
if (year % 400==0 ) and (year% 100 == 0):
    print("Leap year". format(year))
elif (year % 4 == 0 ) and (year % 100  != 0):
    print('Leap year '.format(year))
else:
    print('Not a leap year')