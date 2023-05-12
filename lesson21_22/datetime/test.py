# визначення теперішньої дати і часу
# обрахування інтервалу між двома подіями
# визначення дня тижня, високосного року для будь-якої дати в минулому не раніше року datetime.MINYEAR
# порівнювати дату і час якихось подій за допомогою операторів порівняння
# робота з часовими зонами порівняння подій з врахуванням часових зон і перехід на літній/зимовий час
# перетворення дати/часу в рядок і навпаки
# '01-06-2002' -> 01-06-2002
from datetime import datetime, timedelta
from time import sleep
current_datetime = datetime.now()
print(current_datetime)

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
# sleep(3)
# print('Привіт!')
# sleep(3)
print(current_datetime.date())
print(current_datetime.time())

date1 = datetime(year=2006, month=10, day=30)
print(date1.date())
print(date1.weekday())

next_month = datetime(year=datetime.now().year, month=datetime.now().month + 1, day=datetime.now().day)
print(next_month)

print(current_datetime < next_month)

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
seventh_day_2021 = datetime(year=2021, month=1, day=7, hour=14)
difference = seventh_day_2020 - seventh_day_2019
print(difference.total_seconds())

four_week_interval = timedelta(weeks=4)

print(seventh_day_2021 + four_week_interval)

delta = timedelta(days=50, seconds=27, microseconds=29, milliseconds=2500, minutes=5, hours=8, weeks=7)

print(delta)

ts = seventh_day_2020.timestamp()
date_1970 = datetime(year=1970, month=1, day=1)

ts += 1000_000_000
print(datetime.fromtimestamp(ts))


day = datetime(year=2023, month=5, day=10)
print(day.strftime('%A %d %B %Y'))


s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y'))

