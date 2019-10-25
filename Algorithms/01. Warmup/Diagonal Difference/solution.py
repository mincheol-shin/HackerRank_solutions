def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    # row
    for i in range(len(arr)):
        left_to_right += arr[i][i]
        right_to_left += arr[i][(len(arr)-1)-i]
    return abs(left_to_right - right_to_left)

if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)


