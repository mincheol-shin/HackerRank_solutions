class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:

    def insert(self,head,data):
            p = Node(data)
            # head가 비어있을 경우 노드 삽입
            if head==None:
                head=p
            # head의 다음 노드가 비어있을 경우 노드 삽입
            elif head.next==None:
                head.next=p
            # 비어있지 않은 경우 비어있는 노드 탐색
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                # 비어있는 노드를 찾았으므로 노드 삽입
                start.next=p
            # 헤드값 리턴
            return head

    # head부터 시작해서 노드 출력
    def display(self,head):
        current = head
        # current가 None값일 경우까지 반복
        while current:
            print(current.data,end=' ')
            current = current.next

    # 중복 제거 함수
    def removeDuplicates(self,head):
        # 헤드나 헤드 다음이 None값일 경우 바로 head 리턴
        if head == None or head.next == None:
            return head
        else:
            # 현재 데이터와 다음 데이터 검사 후 같으면 다음 데이터 변경
            self.removeDuplicates(head.next)
            if head.data == head.next.data:
                head.next = head.next.next
        return head



mylist= Solution()
# 노드갯수
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)

head=mylist.removeDuplicates(head)
mylist.display(head);