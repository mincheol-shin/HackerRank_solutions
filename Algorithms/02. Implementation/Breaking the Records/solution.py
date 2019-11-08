def breakingRecords(scores):
    result = {"max" : 0, "min" : 0}
    max = min = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max:
            max = scores[i]
            result["max"] += 1
        elif scores[i] < min:
            min = scores[i]
            result["min"] += 1

    return  result


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(*result.values())
