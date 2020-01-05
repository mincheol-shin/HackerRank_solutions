from collections import Counter

if __name__ == "__main__":
    players = int(input())
    leader_board = list(Counter(map(int, input().split())).keys())
    alice_plays = int(input())
    alice_scores = list(map(int, input().split()))
    # 정렬 알고리즘 사용시 복잡도가 너무 커져서 Test case 6 ~ 10 통과 불가
    # leader board에 대한 사용자 입력은 내림차순, alice score에 대한 사용자 입력은 오름차순
    for i in alice_scores:
        for j in range(len(leader_board)-1, -1, -1):
            if leader_board[j] > i:
                print("{}".format(j+2))
                break
            elif j == 0:
                print("{}".format('1'))
