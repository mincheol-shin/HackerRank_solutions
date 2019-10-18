def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    # 고유 요소이며 크기가 2 이상인 배열 리턴
    @staticmethod
    def get_array():
        return [1,2,3,4,5]

    # 최소값 인덱스 리턴
    @staticmethod
    def get_expected_result():
        return minimum_index(TestDataUniqueValues.get_array())

class TestDataExactlyTwoDifferentMinimums(object):

    # 두 개의 다른 최솟값이 있는 배열 리턴
    @staticmethod
    def get_array():
        return [2,3,4,5,6,1,2]

    # 예상 최솟값 인덱스 리턴 => 아래 코드는 첫 번째 요소만 출력
    @staticmethod
    def get_expected_result():
        return minimum_index(TestDataExactlyTwoDifferentMinimums.get_array())




