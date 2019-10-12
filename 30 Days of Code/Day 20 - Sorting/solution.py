import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numberOfSwaps = 0
# Bubble Sort
for i in range(1, n):
    for j in range(n-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numberOfSwaps += 1

print("Array is sorted in {0} swaps.\nFirst Element: {1}\nLast Element: {2}".format(numberOfSwaps,a[0],a[n-1]))

