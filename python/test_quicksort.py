def partion(arr,lo, mid):
    piv = arr[mid]
    sorted = 0
    for i, item in enumerate(arr):
        if (item <= piv):
            arr[sorted], arr[i] = arr[i], arr[sorted]
            sorted += 1
        if (i > mid):
            arr[sorted -1], arr[mid] = arr[mid], arr[sorted - 1]

    return sorted - 1


def qs(arr, lo, mid):
    if lo>=mid:
        return
    idx = partion(arr,lo,mid)
    qs(arr, lo, idx - 1)
    qs(arr, idx + 1, mid)


def quicksort(arr):
    qs(arr,0, len(arr)// 2)  
    return arr

class TestClass:
    def test_1(self):

        unsorted_array = [
            42, 32, 60, 17, 90, 82, 56, 29, 74, 64, 15, 87, 98, 51, 41, 19, 61, 55, 39, 71, 
           23, 45, 68, 37, 91, 47, 88, 67, 22, 48, 99, 54, 25, 34, 62, 73, 16, 31, 49, 94, 
            81, 33, 21, 85, 46, 72, 11, 59, 53, 76, 40, 57, 13, 79, 24, 65, 93, 43, 27, 89, 
            50, 12, 70, 35, 18, 63, 84, 92, 38, 44, 100, 30, 66, 58, 83, 77, 52, 26, 78, 36, 
            75, 14, 86, 28, 20, 95, 97, 69, 10, 96, 80
        ]

        assert quicksort(unsorted_array) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
        50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
        70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
        90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    def test_2(self):
        assert quicksort([1,0]) == [0,1]
