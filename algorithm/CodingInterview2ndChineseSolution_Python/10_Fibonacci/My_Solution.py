def Fibonacci(n):
    n = int(n)
    result = []
    result.insert(0, 0)
    result.insert(0, 1)
    if (n < 2):
        return result[n]
    else:
        for i in range(2, n + 1):
            result.insert(i, (result[i - 2] + result[i - 1]))
    return result[n]


if __name__ == '__main__':
    print(Fibonacci(11))
