"""
判断一个数是不是2得整数次幂
"""
"""
如果一个整数是2的整数次方，则他二进制中有且只有一个1
"""


def powerOf2(n):
    if n & (n - 1) == 0:
        return True
    else:
        return False


print(powerOf2(1024))
