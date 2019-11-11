def divisibleSumPairs(n: int, k: int, ar: list) -> int:
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count


if __name__ == '__main__':
    n, k = map(int, input().split())

    ar = list(map(int, input().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
