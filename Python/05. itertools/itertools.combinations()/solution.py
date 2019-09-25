from itertools import combinations

S, k = input().split()

for i in range(1, int(k)+1):
    combinations_S = ""
    combinations_S = (list(map("".join,combinations(sorted(S), i))))
    print(*combinations_S, sep = "\n")

