class Solution1:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        flag = False
        for index in range(len(array)):
            if target in array[index]:
                flag = True
        return flag


class Solution2:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        # 标识变量
        found = False
        # 检查输入 None，空数组
        if array == None:
            return found
        nRow = len(array)
        nCol = len(array[0])
        # 右上角位置
        row = 0
        col = nCol - 1
        # 从右上角遍历
        while (row < nRow) and (col >= 0):
            if array[row][col] == target:
                found = True
                break
            elif array[row][col] > target:
                col = col - 1
            else:
                row = row + 1
        return found


def main():
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    array2 = []
    array3 = [['a', 'b', 'c'],
              ['b', 'c', 'd']]
    array4 = [[62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
              [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
              [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
              [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
              [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
              [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]]
    a = Solution1().Find(array=array, target=8)
    print(a)


if __name__ == '__main__':
    main()
