class AdvancedArithmetic(object):
    # 강제 예외 발생
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum = 0
        for i in range(1, n+1):
            # 나머지가 0일 경우 n의 약수
            if n % i == 0:
                sum += i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)