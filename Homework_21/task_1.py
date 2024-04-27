def generate_sequence_normal(n):
    sequence = [n]  # Start the sequence with n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def generate_sequence_with_caching(n, cache={}):
    if n in cache:
        return cache[n]

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    cache[n] = sequence
    return sequence


def main():
    n = int(input("Enter a number: "))
    print("Sequence with normal function:", generate_sequence_normal(n))
    print("Sequence with caching:", generate_sequence_with_caching(n))


if __name__ == '__main__':
    main()
