import re

for _ in range(int(input())):

    try:
        S = re.compile(input())
        print("True")
    except re.error:
        print('False')
