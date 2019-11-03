def countApplesAndOranges(start_point, end_point, apple_tree, orange_tree, apples, oranges):

    # 사과가 떨어진 거리와 나무의 거리를 더한 값이 start_point와 end_point사이에 위치하는가?
    apple, orange = 0, 0
    for i in apples:
        if start_point <= apple_tree + i <= end_point:
            apple += 1
    for i in oranges:
        if start_point <= orange_tree + i <= end_point:
            orange += 1

    return apple, orange






if __name__ == '__main__':
    start_point, end_point = map(int, input().split())
    apple_tree, orange_tree = map(int, input().split())
    number_of_apple, number_of_orange = map(int, input().split()) # Deletion possible
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    result = countApplesAndOranges(start_point, end_point, apple_tree, orange_tree, apples, oranges)

    print(*result, sep = "\n")