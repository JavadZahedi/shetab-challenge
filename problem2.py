from math import sqrt, floor

OUTPUT_FILE = 'primes.txt'

def primes_generator(n):  # Algorithm with order of O(n^(3/2))
    for i in range(2, n):
        for j in range(2, floor(sqrt(i)) + 1):
            if i%j == 0:
                break
        else:
            yield i


def write_to_file(seq):
    with open(OUTPUT_FILE, 'w') as file:
        for x in seq:
            file.write(f'{x}\n')


def main():
    n = 1000000
    seq = primes_generator(n)
    write_to_file(seq)


if __name__ == '__main__':
    main()