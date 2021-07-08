def old_main(): # Non efficient solution
    seq = filter(lambda x: (x%3 == 0 or x%5 == 0), range(1, 1000))
    result = sum(seq)
    print(result)


def multipliers_sum(n, k):
    seq_length = (n-1) // k
    return k * seq_length * (seq_length+1) / 2


def new_main(): # efficient solution
    result = (multipliers_sum(1000, 3) + multipliers_sum(1000, 5)
             - multipliers_sum(1000, 15))
    print(int(result))


if __name__ == '__main__':
    new_main()