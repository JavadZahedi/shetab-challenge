def old_main():  # Non efficient solution in O(n)
    n = 1000
    seq = filter(lambda x: (x%3 == 0 or x%5 == 0), range(1, n))
    result = sum(seq)
    print(result)


def multipliers_sum(n, k):
    seq_length = (n-1) // k
    return k * seq_length * (seq_length+1) / 2


def new_main():  # Efficient solution in O(1)
    n = 1000
    result = (multipliers_sum(n, 3) + multipliers_sum(n, 5)
              - multipliers_sum(n, 15))
    print(int(result))


if __name__ == '__main__':
    new_main()