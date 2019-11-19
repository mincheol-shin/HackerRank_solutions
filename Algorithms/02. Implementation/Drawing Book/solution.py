def pageCount(n, p):
    book = [1, ]
    count = []
    for i in range(2, n, 2):
        book.append([i, i+1])

    if n % 2 == 0:
        book.append(n)

    for i in range(len(book)):
        temp = 0
        for j in range(i+1, len(book)):
            pass
    print(count)
if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print("{}".format(result))


