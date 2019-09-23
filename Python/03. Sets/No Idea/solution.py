n, m = map(int, input().split())
array, A, B = input().split(), set(input().split()), set(input().split())
total_happiness = 0

# array의 요소가 존재한다면 1, 아니면 0 리턴
for i in array:
    total_happiness += (i in A) - (i in B)

print("{}".format(total_happiness))

