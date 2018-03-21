def combine_2_list(a, b):
    c = []
    counta = countb = 0  # 分别记录两个数组遍历到哪个位置了
    for i in range(counta, len(a)):
        for j in range(countb, len(b)):
            if (b[j] <= a[i]):
                c.append(b[j])
                countb = countb + 1  # append了b[j],那么b数组的遍历的记录应该自增
            else:
                c.append(a[i])
                counta = counta + 1  # append了a[i],那么a数组的遍历的记录应该自增
                break  # 为啥要break？因为到此位置，说明b数组不能继续往下遍历了，该遍历a了

        # 现在就需要吧两个数组中剩余的元素依次append到c中即可
    if counta < len(a):
        for i in range(counta, len(a)):
            c.append(a[i])
    if countb < len(b):
        for j in range(countb, len(b)):
            c.append(b[j])
    return c


def main():
    a = [1, 2, 3, 4, 5, 6]
    b = [3, 4, 6, 7, 8]
    count = combine_2_list(a, b)
    print(count)


if __name__ == '__main__':
    main()
