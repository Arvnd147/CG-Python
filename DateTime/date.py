import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2018,6,1)

print(x)

"""
%a - weekday short form
%A - weekday long form
%w - weekday as no. (0-6)
%d - day of month
%b - month name short form
%B - month name long form
%m - month number (1-12)
%y - year short form 
%Y - year long form
%H - year format
"""