class Difference:
    def __init__(self, a):
        self.__elements = a

    maximumDifference = 0
    # 각 자리수를 빼고 최대값과 비교
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(1, len(a)):
                if abs(a[i] - a[j]) > self.maximumDifference:
                    self.maximumDifference = abs(a[i] - a[j])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)