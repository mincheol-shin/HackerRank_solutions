def designer_pdf_viewer(h, word):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    location_num = []
    # word의 문자가 알파벳 몇 번째 위치에 있는지 확인 후 저장
    for i in list(word):
        location_num.append(h[alphabet.find(i)])
    maximum = max(location_num)
    minimum = min(location_num)

    return len(word) * minimum * maximum


if __name__ == '__main__':
    h = list(map(int, input().split()))
    word = input()

    result = designer_pdf_viewer(h, word)

    print("{}".format(result))
