def main():
    n = int(input())
    name_and_numbers = [input().split() for _ in range(n)]
    phone_book = {key:value for key,value in name_and_numbers}
    phone_book_keys = phone_book.keys() # 미리 생성하여 비교 => 메모리 절약?
    for _ in range(n):
        name = input()
        if name in phone_book_keys:
            print("{0}={1}".format(name, phone_book[name]))
        else:
            print("Not found")

if __name__ == "__main__":
    main()