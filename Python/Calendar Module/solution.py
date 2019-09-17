import calendar

month, day, year = map(int, input().split())
day_of_the_week = calendar.weekday(year, month, day)
week_list = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(week_list[day_of_the_week])