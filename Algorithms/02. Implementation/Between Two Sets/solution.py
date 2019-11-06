def getTotalX(a, b):
    first_factor, second_factor = a
    count = 0
    for i in range(first_factor,b[0]+1, first_factor):
        if i % first_factor == 0 and i % second_factor == 0:
            for j in range(len(b)):
                if b[j] % i == 0:
                    if j == len(b) - 1:
                        count += 1
                else:
                    break

    return count
if __name__ == '__main__':

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    total = getTotalX(arr, brr)
    print(total)
