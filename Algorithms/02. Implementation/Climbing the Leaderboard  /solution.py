if __name__ == "__main__":
    players = int(input())
    leader_board = list(set(map(int, input().split())))
    alice_plays = int(input())
    alice_scores = list(map(int, input().split()))
    count = 0
    for i in alice_scores:
        leader_board.append(i)
        leader_board.sort()
        leader_board.reverse()
        print(leader_board.index(i)+1)
