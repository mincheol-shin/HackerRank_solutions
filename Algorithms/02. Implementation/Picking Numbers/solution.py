def pickingNumbers(a):
    maximum = 0
    for i in a:
        # 해당 요소의 개수와 해당 요소에서 1을 뺀 수의 개수를 더하면 최대값이 나온다.
        element_count = a.count(i)
        compare_element_count = a.count(i-1)

        if (maximum < element_count + compare_element_count):
            maximum = element_count + compare_element_count

    return maximum



if __name__ == '__main__':

    n = int(input())
    a = list(map(int, input().split()))

    result = pickingNumbers(a)

    print(result)
