from collections import namedtuple

# 학생수
N = int(input())
column_name = namedtuple("column",input().split())
total_score = []

for i in range(N):
    info = column_name._make(input().split())
    total_score.append(int(info.MARKS))

print("{:.2f}".format(sum(total_score) / len(total_score)))