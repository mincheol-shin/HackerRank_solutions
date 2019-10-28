def timeConversion(s):

    hour, minute, second = s.split(":")
    hour = int(hour)
    second, am_pm = second[0:2], second[2:4]

    if am_pm == "AM":
        if hour == 12:
            return "00" + ":" + minute + ":" + second
    else:
        if hour >= 12:
            pass
        else:
            hour += 12

    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    return str(hour) + ":" + minute + ":" + second



if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)
