import math

if __name__ == "__main__":

    # 테스트 케이스 수
    T = int(input())
    # 절반정도까지 비교한다.
    for i in range(T):
        case = int(input())
        # 연산에서 time limits 발생하여 수정
        half_of_case = int(math.sqrt(case)) + 1
        count = 0 # 1외의 다른 숫자로 나누어지는지 판단
        if case == 1:
            print("Not prime")
            continue

        for j in range(2, half_of_case):
            if case % j == 0:
                count += 1
        if count == 0:
            print("Prime")
        else:
            print("Not prime")




