
# Complete the compareTriplets function below.
def compareTriplets(a, b):

    Alice = [i for i in range(len(a)) if a[i] > b[i]]
    Bob = [i for i in range(len(b)) if b[i] > a[i]]
    return (len(Alice), len(Bob))


if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(*result)
