if __name__ == '__main__':

    test_case = int(input())
    for i in range(test_case):
        student, standard = map(int, input().split())
        arrived_time = [i for i in map(int, input().split()) if i <= 0]

        print("{}".format("YES" if len(arrived_time) < standard else "NO"))