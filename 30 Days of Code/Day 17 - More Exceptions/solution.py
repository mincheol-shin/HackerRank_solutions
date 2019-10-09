class Calculator():

    def __init__(self):
        pass

    def power(self, n: int, p: int):
        if (n >= 0) and (p >= 0):
            return n ** p
        # 예외 발생시키기
        else:
            raise Exception('n and p should be non-negative')


myCalculator = Calculator()
T = int(input())
for i in range(T):
    # 두 수를 한 줄에 입력받고 형변환
    n,p = map(int, input().split())

    try:
        ans = myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)