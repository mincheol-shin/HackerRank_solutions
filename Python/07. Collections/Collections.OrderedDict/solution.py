from collections import OrderedDict

ordinary_dictionary = OrderedDict()
N = int(input())

for _ in range(N):
    # 문자열입력 받은 후 자르기
    item = input().split()
    item_name = ' '.join(item[0:len(item)-1])
    net_price = item[-1]
    # 초기값 설정
    ordinary_dictionary.setdefault(item_name, 0)
    ordinary_dictionary[item_name] += int(net_price)

for k, v in ordinary_dictionary.items():
    print("{} {}".format(k,v))