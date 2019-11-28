def pageCount(n, p):
    book = [[1], ]
    count = 0
    reversed_count = 0
    for i in range(2, n, 2):
        book.append([i, i + 1])

    if n % 2 == 0:
        book.append([n])

    for i in range(len(book)):
        if p in book[i]:
           break
        count += 1

    for i in range(-1, -len(book)-1, -1):
        if p in book[i]:
           break
        reversed_count += 1


    return reversed_count if count > reversed_count else count


if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print("{}".format(result))
