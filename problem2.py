from math import sqrt, ceil, floor

OUTPUT_FILE = 'primes.txt'

def get_prime_numbers(n):
    seq = []
    for i in range(2, n):
        for j in range(2, floor(sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            seq.append(i)
    return seq


def write_to_file(seq):
    with open(OUTPUT_FILE, 'w') as file:
        for x in seq:
            file.write(f'{x}\n')


def main():
    n = 50
    seq = get_prime_numbers(n)
    write_to_file(seq)


if __name__ == '__main__':
    main()