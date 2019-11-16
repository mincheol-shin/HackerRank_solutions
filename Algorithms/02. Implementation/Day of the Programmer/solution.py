import calendar

def dayOfProgrammer(year)-> str:
    february = 0
    seven_months = 215 # 2월을 제외한 모든 날의 합은 같다.
    day_of_the_programmer = 256

    # Julian calendar 28(leap year : 29)
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            february = 29
        else:
            february = 28
    # Gregorian calendar
    if year >= 1919:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            february = 29
        else:
            february = 28
    if year == 1918:
        february = 15

    result = day_of_the_programmer-(seven_months + february)
    return "{}.09.{}".format(result,year)

if __name__ == '__main__':

    year = int(input())

    result = dayOfProgrammer(year)

    print("{}".format(result))