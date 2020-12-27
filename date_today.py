from datetime import date
import calendar
my_date = date.today()
my_day = my_date.day
my_month = my_date.month

if my_month == 12 and my_day == 25:
    print('Merry Gitmas!')
elif my_month == 12 and my_day > 25:
    my_string = 'This the ' + str(my_day-24) + ' day of Christmas!'
    print(my_string)