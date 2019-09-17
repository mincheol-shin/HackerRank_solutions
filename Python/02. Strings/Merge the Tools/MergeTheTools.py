def merge_the_tools(string: str, k: int):

    string_length = len(string)
    answer_list = []
    position = 0
    for i in range(0,string_length+1,k):
        if i is not 0:
            answer_list.append(list(dict.fromkeys(string[position:i])))
            position = i

    for i in range(len(answer_list)):
        print("".join(answer_list[i]))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

