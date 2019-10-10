from collections import deque

class Solution:

    __slots__ = ["stack", "queue"]

    def __init__(self):
        self.stack = []
        self.queue = deque()

    # 큐와 스택에 데이터 삽입
    def pushCharacter(self, ch: str):
        self.stack.append(ch)

    def enqueueCharacter(self, ch: str):
        self.queue.append(ch)

    # 큐와 스택에서 데이터 추출
    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()

s = input()
obj = Solution()
l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")