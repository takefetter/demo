# Python3
# 58转转面试题,判断两个数组元素是否完全相同
def is_the_same(a, b):
    if len(a) < 0 or len(b) < 0 or len(a) != len(b):
        return False
    a.sort()
    b.sort()
    # 这里可以替换成排序算法 如快排,时间复杂度为O(nlogn)
    # Python中的sort会改变原数组顺序,不知道这个影响题意否...
    for i in range(len(a)):
        if a[i] != b[i]:  # 这步时间复杂度为O(n)
            return False

    return True


a = [1, 1, 2, 3, 4]
b = [1, 2, 4, 5]
c = [1, 2, 1, 3, 4]
d = [1, 2, 3]
result = is_the_same(a, b)
print(result)
result = is_the_same(a, c)
print(result)
result = is_the_same(a, d)
print(result)
