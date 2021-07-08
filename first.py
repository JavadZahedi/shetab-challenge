def main():
    seq = filter(lambda x: (x%3 == 0 or x%5 == 0), range(1, 1000))
    result = sum(seq)
    print(result)


if __name__ == '__main__':
    main()