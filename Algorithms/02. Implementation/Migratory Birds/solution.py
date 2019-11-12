def migratoryBirds(arr):
    num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for i in arr:
        num[i] += 1
    return list(num.keys())[list(num.values()).index(max(num.values()))]


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().split()))

    result = migratoryBirds(arr)
    print(result)
