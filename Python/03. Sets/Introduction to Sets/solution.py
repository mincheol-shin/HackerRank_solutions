def average(array):
    array = set(array)
    array_length = len(array)
    sum_array = sum(array)
    average_array = float(sum_array / array_length)

    return average_array

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)