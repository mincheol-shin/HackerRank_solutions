if __name__ == "__main__":

    n, k, q = map(int, input().split())
    array = list(map(int, input().split()))

    # 인덱스와 회전하는 수의 공식을 구하면 해겷할 수 있지 않을까?
    
    for i in range(k):
        temp = array[-1]
        array.remove(array[-1])
        array.insert(0, temp)

    for i in range(q):
        element_index = int(input())
        print(array[element_index])

