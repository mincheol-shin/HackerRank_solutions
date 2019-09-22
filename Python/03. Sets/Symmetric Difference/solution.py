
a = set()
b = set()

# 한 줄에 입력받은 수를 int형으로 update
M = int(input())
a.update(map(int,input().split()))

N = int(input())
b.update(map(int,input().split()))

# a와 b 각각의 차집합을 더한 뒤 list형으로 만들고 정렬
result = sorted(list((a.difference(b)).union(b.difference(a))))

print(*result, sep = "\n")