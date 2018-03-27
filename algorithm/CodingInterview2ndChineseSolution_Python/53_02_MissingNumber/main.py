'''
查找递增数组中缺失的数字(二分查找)
'''
class solution:
    def GetMissintNumber(self, numbers, length):
        if numbers == None or length <= 0:
            return -1
        left = 0
        right = length - 1
        while (left <= right):
            middle = (right + left) >> 1
            if (numbers[middle] != middle):
                if middle == 0 or numbers[middle - 1] == middle - 1:
                    return middle
                right = middle - 1
            else:
                left = middle + 1
        if left == length:
            return length

        return -1
