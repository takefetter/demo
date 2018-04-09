# Python3
def subset(items):
    if len(items) == 0:
        return [[]]

    subsets = []
    first_elt = items[0]
    rest_list = items[1:]

    for partial_subset in subset(rest_list):
        subsets.append(partial_subset)
        next_subset = [first_elt] + partial_subset[:]
        subsets.append(next_subset)
    return subsets


if __name__ == '__main__':
    result = subset([1, 2, 3])
    print(result)  # 输出结果[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] 考虑到了空集的情况
