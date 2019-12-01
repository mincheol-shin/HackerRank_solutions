def getMoneySpent(keyboards, drives, budget):
    result = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sum_price = keyboards[i] + drives[j]
            if result < sum_price <= budget:
                result = sum_price
    # over budget
    if result == 0:
        result -= 1

    return result


if __name__ == '__main__':
    budget, n, m = map(int, input().split())
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))
    moneySpent = getMoneySpent(keyboards, drives, budget)

    print(moneySpent)
