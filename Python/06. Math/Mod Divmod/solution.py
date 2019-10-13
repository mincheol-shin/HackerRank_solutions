if __name__ == "__main__":

    a, b = int(input()), int(input())

    # a를 b로 나눈 몫과 나머지를 리턴
    result = divmod(a,b)

    # 결과 출력
    print("{0}\n{1}\n{2}".format(result[0],result[1],result))