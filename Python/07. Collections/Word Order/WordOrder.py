from collections import OrderedDict, Counter

patterns = OrderedDict([[i,pattern] for i, pattern in enumerate([input() for _ in range(int(input()))])])
patterns_values = Counter(patterns.values())
patterns_length = len(patterns_values)
print("{}".format(patterns_length))
print(*patterns_values.values())


'''
time limits

def main():

    number_of_inputs = int(input())
    input_patterns = [input() for _ in range(number_of_inputs)]
    number_of_discrepancies = number_of_inputs
    count_patterns = []

    for i in range(0, number_of_inputs):
        if input_patterns[0] == input_patterns[i] and i is not 0:
            number_of_discrepancies -= 1

        if input_patterns[i] is not None:
            pattern_count = input_patterns.count(input_patterns[i])
            count_patterns.append(str(pattern_count))

        if pattern_count > 1:
            temp = input_patterns[i]
            for _ in range(pattern_count):
                same_pattern_index = input_patterns.index(temp)
                input_patterns[same_pattern_index] = None

    print("{}\n{}".format(number_of_discrepancies," ".join(count_patterns)))

if __name__ == "__main__":

    main()

'''