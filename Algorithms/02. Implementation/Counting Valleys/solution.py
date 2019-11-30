def countingValleys(n, s):
    count = 0
    current_location = 0
    for i in s:
        if i == "U":
            current_location += 1
            if current_location == 0:
                count += 1
        else:
            current_location -= 1

    return count

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)

