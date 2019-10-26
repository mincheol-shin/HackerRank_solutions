

def plusMinus(arr):
    positive , negative , zeros = 0, 0, 0
    array_length = len(arr)
    for i in arr:
        if i > 0:
            positive += 1
        elif i == 0:
            zeros += 1
        else:
            negative += 1

    print("{0:5f}".format(positive/array_length))
    print("{0:5f}".format(negative/array_length))
    print("{0:5f}".format(zeros/array_length))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
