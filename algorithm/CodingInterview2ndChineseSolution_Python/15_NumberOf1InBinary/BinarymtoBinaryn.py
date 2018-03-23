"""
判断两个数的二进制表示有多少位不一样
"""
"""
先求两个数的异或，再比较两个数的二进制异或就可以
"""


def andor(m, n):
    diff = m ^ n  # 异或操作,同位清零
    count = 0
    while diff:
        count += 1
        diff = diff & (diff - 1)
    return count


count = andor(0xFFFFF, 0x2FFFF)
print(count)
