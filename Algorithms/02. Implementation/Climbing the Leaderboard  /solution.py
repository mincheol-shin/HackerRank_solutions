if __name__ == "__main__":
    players = int(input())
    leader_board = sorted(list(set(map(int, input().split()))))
    alice_plays = int(input())
    alice_scores = list(map(int, input().split()))
    leader_board.reverse()
    for i in alice_scores:
        for j in range(len(leader_board)):
            if i >= leader_board[j]:
                print(j + 1)
                break
            if j + 1 == len(leader_board):
                print(j + 2)

