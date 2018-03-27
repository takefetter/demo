'''
单调递增数组中数值和下标相等的元素
'''


class Solution:
    def GetNumberSameAsIndex(self, numbers, length):
        if numbers == None or length < 0:
            return -1

        left = 0
        right = 0
        while left <= right:
            middle = left + (right - left) >> 1
            if (numbers[middle] == middle):
                return middle
            if (numbers[middle] > middle):
                right = middle - 1
            else:
                left = middle + 1

        return -1
