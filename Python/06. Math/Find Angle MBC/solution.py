from math import *

# Arc Tangent 이용, 두 변의 길이를 이용해 각도 구하기
# M은 원의 중점, MB와 MC의 길이는 반지름으로 길이가 같으며 이등변 삼각형으로 MBC와 MCB의 각은 같다.
AB, BC = int(input()), int(input())
MBC = atan2(AB, BC)
print((str(round(degrees(MBC)))+'°'))
