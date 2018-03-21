def main():
    ids = [1, 2, 3, 3, 4, 2, 3, 4, 5, 6, 1]
    print(ids)

    news_ids = []
    for id in ids:
        if id not in news_ids:
            news_ids.append(id)

    print(news_ids)


if __name__ == '__main__':
    main()
