def main():
    ids = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
    news_ids = []
    duplicationarray = []
    for id in ids:
        if id not in news_ids:
            news_ids.append(id)
        elif id in news_ids and id not in duplicationarray:
            duplicationarray.append(id)
        else:
            pass
    print(ids)
    print(news_ids)
    print(duplicationarray)


if __name__ == '__main__':
    main()
