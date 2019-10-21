if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        if k | k-1 > n:
            print("{}".format(k-2))
        else:
            print("{}".format(k-1))
'''
# time out
def bitwise_and(size: int, maximum_possible: int):
    S = [i for i in range(1, size+1)]
    max = 0
    for i in range(size):
        for j in range(i+1, size):
            result = S[i] & S[j]
            if maximum_possible > result and result > max:
                max = result
    return max

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print("{}".format(bitwise_and(n,k)))
'''
