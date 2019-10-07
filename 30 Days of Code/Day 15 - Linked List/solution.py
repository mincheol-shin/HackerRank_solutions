class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self,head,data):

        # head가 None값일 경우 지정
        if head is None:
            head = Node(data)
        # head의 next값이 None일 경우 next값 지정
        elif head.next is None:
            head.next = Node(data)
        # head가 None이 아니고, next값이 None이 아닐경우 다음노드 탐색
        else:
            self.insert(head.next, data)

        return head

if __name__ == "__main__":
    mylist = Solution()
    T = int(input())
    head = None

    # T만큼 반복해서 data입력, i는 언더스코어 대체가능
    for i in range(T):
        data = int(input())
        head = mylist.insert(head,data)

    mylist.display(head);