def binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while (lo < hi):
        mid = lo + (hi - lo) // 2
        mid_char = arr[mid]
        if mid_char == target:
            return mid
        if mid_char > target:
            hi = mid
        else:
            lo = mid + 1

    return -1


class TestClass:
    def test_one(self):
        array1 = [1, 4, 7, 8, 10]
        assert binary_search(array1, 7) == 2
        assert binary_search(array1, 5) == -1

    def test_two(self):
        array2 = [3, 9, 14, 15, 18, 22, 27, 31]
        assert binary_search(array2, 15) == 3
        assert binary_search(array2, 11) == -1

    def test_three(self):
        array3 = [0, 4, 8, 12, 15, 18, 21, 25, 29, 34,
                  38, 42, 45, 47, 50, 54, 57, 60, 63, 67]
        assert binary_search(array3, 34) == 9
        assert binary_search(array3, 100) == -1
