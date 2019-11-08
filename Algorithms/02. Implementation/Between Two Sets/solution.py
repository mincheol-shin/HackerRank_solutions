def getTotalX(a, b):
    total = 0
    # Minimize iteration
    for i in range(min(a), min(b) + 1, min(a)):
        if all(i % a_element == 0 for a_element in a) and all(b_element % i == 0 for b_element in b):
            total += 1
    return total


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    total = getTotalX(arr, brr)
    print(total)
