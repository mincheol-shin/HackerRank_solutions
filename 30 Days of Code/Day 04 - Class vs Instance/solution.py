class Person:

    __slots__ = ["initialAge"]

    def __init__(self,initialAge):
       self.initialAge = initialAge

    def amIOld(self):

        # 나이 구분
        if self.initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")
        if self.initialAge < 13:
            print("You are young.")
        elif self.initialAge >= 13 and self.initialAge < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
       self.initialAge += 1

if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        age = int(input())
        p = Person(age)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")