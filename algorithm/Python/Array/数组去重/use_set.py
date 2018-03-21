def main():
    ids = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
    print(ids)
    id = set(ids)  # 不会保留原有顺序
    id = list(id)
    print(id)


if __name__ == '__main__':
    main()
