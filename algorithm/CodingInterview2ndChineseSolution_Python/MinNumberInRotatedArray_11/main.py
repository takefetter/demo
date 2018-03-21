'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''


# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        '''
        if len(rotateArray) == 1:
            return rotateArray[0];
        '''
        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1
        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) // 2
            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid
            elif rotateArray[indexMid] <= rotateArray[index2]:
                index2 = indexMid
        return rotateArray[indexMid]


if __name__ == '__main__':
    a = Solution()
    b = a.minNumberInRotateArray([3, 4, 5, 1, 2])
    print(b)
