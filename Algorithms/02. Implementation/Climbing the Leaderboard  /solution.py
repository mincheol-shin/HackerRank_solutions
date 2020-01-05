if __name__ == "__main__":
    players = int(input())
    leader_board = list(map(int, input().split()))
    alice_plays = int(input())
    alice_scores = list(map(int, input().split()))
    # 정렬 알고리즘 사용시 복잡도가 너무 커져서 Test case 6 ~ 10 통과 불가
    # 사용자의 입력이 정렬된 상태임을 파악

    for i in alice_scores:
        count = 0
        for j in range(len(leader_board)):
            if j > 0:
                if leader_board[j] == leader_board[j-1]:
                    count +=1
            if i >= leader_board[j]:
                print("{0}".format(j+1-count))
                break
            if j+1 == len(leader_board):
                print("{}".format((j+2)-count))