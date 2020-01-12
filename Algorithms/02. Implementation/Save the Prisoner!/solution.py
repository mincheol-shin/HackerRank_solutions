if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n, m, s = map(int, input().split())

        # 사탕 갯수를 사람의 수로 나눈 나머지와 시작점에서 1을 뺀 수를 더함
        result = (m % n) + (s - 1)

        # 결과값이 사람의 수보다 크다면 초과한 것이므로 빼준다.
        if result > n:
            print("{}".format(result - n))
        else:
            if result == 0:
                if (n + (s - 1)) > n:
                    print("{}".format(0 + (s - 1)))
                else:
                    print(n + (s - 1))
            else:
                print("{}".format(result))
