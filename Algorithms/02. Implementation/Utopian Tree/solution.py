def utopian_tree(n: int):
    height = 1
    # n만큼 반복, 주기는 봄 -> 여름 -> (새로운) 봄 -> 여름 ...
    #
    if n > 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                height += 1
            elif i % 2 == 1 and i == 1:
                height += 1
            else:
                height *= 2

    else:
        pass

    print(height)


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        utopian_tree(n)
