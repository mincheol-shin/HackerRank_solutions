def miniMaxSum(arr):
    max = 0
    min = sum(arr)  # 초기값 설정

    for i in arr:
        temp = sum(arr) - i
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    print("{0} {1}".format(min, max))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
