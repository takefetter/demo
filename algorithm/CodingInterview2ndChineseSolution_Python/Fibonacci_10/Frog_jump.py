# 青蛙跳台阶可跳1/2级,求该青蛙跳上一个n级台阶总共有多少种跳法
# -*- coding:utf-8 -*-
def Solution(n):
    if (n < 0):
        return -1
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    return Solution(n - 2) + Solution(n - 1)


class Solution2:
    def jumpFloorII(self, number):
        # write code here
        # 规律：f(n) = 2^(n-1)
        return 2 **(number - 1)


if __name__ == '__main__':
    print(Solution(10))
    print(Solution2().jumpFloorII(5))
