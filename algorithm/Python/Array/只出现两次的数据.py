def main(list1):
    a = set()
    b = set()
    for i in range(len(list1)):
        if list1[i] not in a:
            a.add(list1[i])
        else:
            b.add(list1[i])

    print(a)
    print(b)


if __name__ == '__main__':
    ids = [1, 2, 3, 3, 4, 2, 4, 5, 6, 1]
    main(ids)
