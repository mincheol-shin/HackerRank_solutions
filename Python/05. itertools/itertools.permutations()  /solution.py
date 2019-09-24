import itertools
# Enter your code here. Read input from STDIN. Print output to STDOUT

S, K = map(str,input().split())
S = list(map(''.join, itertools.permutations(sorted(S),int(K))))

for i in range(len(S)):
    print("{}".format(S[i]))

