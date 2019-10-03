if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    total = []
    for i in range(4):
        for j in range(4):
            # 세 줄의 규칙을 미리 만들어서 더함
            first_line = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            second_line = arr[i+1][j+1]
            third_line = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            # 미리 최댓값 비교 후 저장하는 방법과 다 저장한 후 최댓값을 찾는 방법 중 어느 방법이 효율적일까?
            total.append(first_line+second_line+third_line)

    print(max(total))
