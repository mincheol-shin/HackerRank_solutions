from functools import singledispatch

int_array = []
str_array = []

@singledispatch
def printArray(num):
    pass

@printArray.register(int)
def _(num):
    int_array.append(num)
@printArray.register(str)
def _(num):
    str_array.append(num)

if __name__ == "__main__":

    for _ in range(int(input())):
        printArray(int(input()))

    for _ in range(int(input())):
        printArray(input())

    print("{0}\n{1}".format(" ".join(map(str,int_array))," ".join(str_array)))