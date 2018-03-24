# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

        # write code here 一开始写成蛇形了-.-
        # result = []
        # cols = len(matrix)
        # rows = len(matrix[0])
        # count = 0
        # for j in range(cols):
        #     if count % 2 == 0:
        #         for i in range(rows):
        #             result.append(matrix[j][i])
        #     else:
        #         for i in range(rows):
        #             result.append(matrix[j][rows - i - 1])
        #     count += 1
        # return result
