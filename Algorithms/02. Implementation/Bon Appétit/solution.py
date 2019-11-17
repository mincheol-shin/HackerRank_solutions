def bonAppetit(bill, k, b):

    total_price = sum(bill) - bill[k]

    if total_price / 2 == b:
        print("Bon Appetit")
    else:
        print("{}".format(int(abs((total_price / 2)-b))))



if __name__ == '__main__':
    n, k = map(int,input().split())

    bill = list(map(int, input().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
