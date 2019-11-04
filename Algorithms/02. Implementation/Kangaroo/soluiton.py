def kangaroo(kangaroos):
    k1, k1_jump, k2, k2_jump = kangaroos
    # k2 > k1
    if k2_jump >= k1_jump:
        return "NO"
    else:
        for _ in range(10000):
            k1 += k1_jump
            k2 += k2_jump

            if k1 == k2:
                return "YES"
            elif k1 > k2:
                return "NO"

if __name__ == '__main__':
    kangaroos_info = map(int, input().split())

    result = kangaroo(kangaroos_info)

    print("{}".format(result))
