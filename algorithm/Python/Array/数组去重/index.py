def main():
    ids = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
    print(ids)
    news_ids = list(set(ids))
    news_ids.sort(key=ids.index)
    print(news_ids)


if __name__ == '__main__':
    main()
