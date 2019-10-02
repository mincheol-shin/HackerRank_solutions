if __name__ == '__main__':
    n = int(input())
    binary_number_list = []
    maximum_number = 0

    # 2진수로 변환
    while n != 0:
        i = n % 2
        binary_number_list.append(str(i))
        n = n // 2
    binary_number_list.reverse()

    # 0을 만나면 0으로 초기화 후에 최댓값 저장
    for i in binary_number_list:
        count = 0
        if i == '1':
            count += 1
        else:
            count = 0

        if maximum_number < count:
            maximum_number = count

    print("{0}".format(maximum_number))