from math import ceil, floor

def get_sum_of_divisors(n: int) -> int:
    divisors = filter(lambda x: n%x == 0, range(1, floor(n/2)+1))
    return sum(divisors)


def is_abundant(n: int) -> bool:
    return get_sum_of_divisors(n) > n


def get_abundants_under(n: int) -> tuple:
    return tuple(filter(lambda x: is_abundant(x), range(12,n)))

LIMIT = 28123

def main():
    abundants = get_abundants_under(LIMIT)
    can_be_written_to_sum_of_two_abundants = [False] * LIMIT
    for a1 in abundants:
        for a2 in abundants:
            if a1+a2 <= LIMIT:
                can_be_written_to_sum_of_two_abundants[a1+a2-1] = True

    numbers = filter(
        lambda x: not can_be_written_to_sum_of_two_abundants[x-1],
        range(24, LIMIT)
    )
    print(sum(numbers))


if __name__ == '__main__':
    main()