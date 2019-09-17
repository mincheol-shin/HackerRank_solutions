def is_leap(year):
    leap = False
    if ((year % 4) == 0):
        if ((year % 100) != 0):
            leap = True
        elif ((year % 400) == 0):
            leap = True
    # Write your logic here

    return print("{}".format(leap))

if __name__ == "__main__":
    year = int(input())
    is_leap(year)