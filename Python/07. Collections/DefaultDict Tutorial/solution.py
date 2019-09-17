from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

# 딕셔너리에 Key, Value 추가
for i in range(n):
    d[input()].append(str(i+1))

# m만큼 입력받아 딕셔너리 체크 문자 입력받기
check_list = [input() for _ in range(m)]

# list 요소 개수만큼 반복하여 딕셔너리에 요소가 있는지 판단
for i in check_list:
    if i in d:
        print("{}".format(" ".join(d[i])))
    else:
        print("{}".format("-1"))