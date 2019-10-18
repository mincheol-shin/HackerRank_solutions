ad, am, ay = map(int, input().split())
ed, em, ey = map(int, input().split())

# 늦게 냈을 경우와 더 빨리 냈을 경우를 생각해야하는 문제
if ay > ey:
    print("{}".format(10000))
elif ay == ey:
    if am > em:
        print("{}".format((am-em)*500))
    elif am >= em and ad > em:
        print("{}".format((ad-ed)*15))
    else:
        print("{}".format(0))
else:
    print("{}".format(0))
