
def catAndMouse(x, y, z):
    cat_a = abs(x-z)
    cat_b = abs(y-z)

    if cat_a > cat_b:
        print("Cat B")
    elif cat_a < cat_b:
        print("Cat A")
    else:
        print("Mouse C")

if __name__ == '__main__':

    q = int(input())

    for i in range(q):
        x, y, z = map(int, input().split())
        catAndMouse(x, y, z)