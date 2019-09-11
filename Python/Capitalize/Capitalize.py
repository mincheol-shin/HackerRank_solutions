#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the solve function below.
def solve(s):
    for x in s.split():
        # replace 교체 => 한 개의 단어를 capitalize()
        s = s.replace(x, string.capwords(x,sep = ","))
    return s
    '''
    s = s.split()
    string = ""
    # 리스트형을 string형으로 변환하니 괄호까지 전부 변환되는 사실
    for i in range(len(s)):
        string += s[i].capitalize() + " "
    return string
    '''

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)