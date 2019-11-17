
def sockMerchant(n, ar):

    pairs = {}
    count = 0
    for i in ar:
        # 값이 존재할 경우
        if i in pairs:
            pairs[i] += 1
        # 존재하지 않을 경우 키 추가
        else:
            pairs[i] = 1

        if pairs[i] == 2:
            pairs[i] = 0
            count += 1

    return count
S
if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().split()))

    result = sockMerchant(n, ar)

    print(result)

