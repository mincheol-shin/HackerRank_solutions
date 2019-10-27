def birthdayCakeCandles(ar):
    max = 0
    count = 0
    
    for i in ar:
        if i > max:
            count = 1
            max = i
        elif i == max:
            count += 1

    return count

if __name__ == '__main__':

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(result)
