def Solution(a):
    count = 0
    array = []
    if a < 1:
        return False
    while (a != 1):
        array.insert(0, a)
        if a % 2 == 1:
            a = a - 1
        else:
            a = a / 2
        a = int(a)
        count += 1;

    print(array)
    return count


if __name__ == '__main__':
    count_ = Solution(10000)
    print(count_)
