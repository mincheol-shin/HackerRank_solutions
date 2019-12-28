def hurdleRace(k, height):
    maximum = max(height)
    if (k < maximum):
        maximum = abs(maximum - k)
    else:
        maximum = 0

    return maximum


if __name__ == '__main__':
    n, k = map(int, input().split())

    height = list(map(int, input().split()))

    result = hurdleRace(k, height)

    print("{}".format(result))
