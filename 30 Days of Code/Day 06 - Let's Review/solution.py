
# 입력받은 수만큼 문자열 입력받기
S = [input() for i in range(int(input()))]

# 홀수와 짝수로 나눠서 출력
for i in range(len(S)):
    print("{0} {1}".format(S[i][0:len(S[i]):2], S[i][1:len(S[i]):2]))