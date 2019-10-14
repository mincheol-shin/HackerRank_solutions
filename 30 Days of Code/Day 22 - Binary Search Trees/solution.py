## Answer
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        left_height = 0
        right_height = 0
        if root.left != None:
            left_height = self.getHeight(root.left) + 1
        if root.right != None:
            right_height = self.getHeight(root.right) + 1

        return max(left_height, right_height)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)

## Binary Search Tree
'''
class Node:

    __slots__ = ["data", "leftChild", "rightChild"]

    # data와 자식노드
    def __init__(self, data):
        self.data = int(data)
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:

    __slots__ = ["root", "height", "count"]

    # 루트
    def __init__(self):
        self.root = None
        # 높이는 노드가 1개일때 0, 2,3 개일때 1, 4,5,6,7일때 2 => //2 한 결과값?
        self.height = 0

    def insert(self, data):
        self.height += 1
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)


    def _insert(self, parentNode, data):
        # 데이터가 기존의 노드데이터보다 작을경우
        if parentNode.data > int(data):
            # 왼쪽 자식노드 존재시 왼쪽 자식노드를 기준으로 다시 비교
            if parentNode.leftChild:
                self._insert(parentNode.leftChild, data)
            # 왼쪽 자식노드가 없을경우 Node 삽입
            else:
                parentNode.leftChild = Node(data)
        # 데이터가 기존의 노드데이터보다 클경우
        else:
            # 존재시 오른쪽 자식노드를 기준으로 다시 비교
            if parentNode.rightChild:
                self._insert(parentNode.rightChild, data)
            # 오른족 자식노드가 없을경우 Node 삽입
            else:
                parentNode.rightChild = Node(data)

    def getHeight(self):
        return self.height // 2

    def getNode(self, root):

        Nodes = []
        # 가장 바깥쪽 iterable의 모든 항목 삽입
        if root.leftChild != None:
            Nodes.extend(self.getNode(root.leftChild))
        if root != None:
            Nodes.append(root.data)
        if root.rightChild != None:
            Nodes.extend(self.getNode(root.rightChild))

        return Nodes

if __name__ == "__main__":

    n = int(input())
    if n > 0:
        binary_search_tree = BinarySearchTree()
    # char -> 1byte, int -> 4byte
        for i in range(n):
            binary_search_tree.insert(input())

        print(binary_search_tree.getHeight())
        print(binary_search_tree.getNode(binary_search_tree.root))
'''