T = int(input())

for _ in range(T):
    try:
        a, b = map(int,input().split())
        print("{}".format(int(a/b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: {}".format(e))


