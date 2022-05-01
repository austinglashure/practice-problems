import datetime
from multiprocessing.dummy import current_process

current_year = datetime.date.today().year

i = 0
leap_years = []

while len(leap_years) < 20:
    if current_year%4 == 0:
        if current_year%100 == 0:
            if current_year%400 == 0:
                leap_years.append(current_year)
        else:
            leap_years.append(current_year)
    current_year += 1

for leap in leap_years:
    print(leap)


