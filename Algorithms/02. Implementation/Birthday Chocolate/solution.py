def birthday(s, d, m):
    chocolate_bar = len(s)
    chocolate_squares = s
    birth_day, birth_month = d, m
    count = 0
    for i in range(0, len(s)):
        if i + birth_month < len(s):
            if sum(chocolate_squares[i:i + birth_month]) == birth_day:
                count += 1

    return count


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))

    d, m = map(int, input().split())

    result = birthday(s, d, m)

    print(result)
