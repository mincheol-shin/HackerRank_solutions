

if __name__ == "__main__":

    i, j, k = map(int,input().split())
    beautiful_day = 0
    range_days = [i for i in range(i, j+1)]
    for i in range_days:
        if str(abs(i-int(str(i)[::-1])) / k)[-1] == '0':
            beautiful_day += 1

    print(beautiful_day)



