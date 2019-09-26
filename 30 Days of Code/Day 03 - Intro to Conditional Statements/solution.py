
import math
import os
import random
import re
import sys

def main():
    N = int(input())

    if N % 2 == 1 or 6 <= N <= 20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    main()