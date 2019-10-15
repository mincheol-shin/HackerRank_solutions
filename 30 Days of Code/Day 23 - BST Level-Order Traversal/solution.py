import sys
from queue import Queue
## BFS

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
# 문제에서는 queue를 사용하지 못하지만 queue 사용이 더 좋다.
class Solution:

    def insert(self,root,data):
        # root가 존재하지 않을 경우 root 생성
        if root==None:
            return Node(data)
        else:
            # 데이터가 루트값보다 작을경우 왼쪽에 삽입
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            # 데이터가 루트값보다 클경우 오른쪽에 삽입
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        # root를 리턴해줘야 왼쪽이나 오른쪽 노드가 무엇인지 알 수 있다.
        return root

    def levelOrder(self,root):
        queue = Queue()
        queue.put(root)
        # queue에 데이터가 존재하는 경우 계속 반복
        while queue.qsize():
            node = queue.get()
            print("{}".format(node.data), end=' ')
            # 왼쪽 노드가 있을 경우
            if node.left != None:
                queue.put(node.left)
            # 오른쪽 노드가 있을 경우
            if node.right != None:
                queue.put(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
