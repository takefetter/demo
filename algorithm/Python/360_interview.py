# Python3
# 360面试题 斐波那契数列
def Fibonacci(n):
    n = int(n)
    temp = [1, 1]
    if n <= 0:
        return None
    if n <= 2:
        return temp[n - 1]
    else:
        for i in range(2, n):
            temp.insert(i, (temp[i - 2] + temp[i - 1]))
        return temp[n - 1]


result = Fibonacci(1)
print(result)
result = Fibonacci(5)
print(result)
result = Fibonacci(-1)
print(result)
result = Fibonacci(0)
print(result)
