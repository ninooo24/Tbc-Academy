def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    print("Is 5 prime number?", is_prime(7))
    print("Is 8 prime number?", is_prime(8))


if __name__ == "__main__":
    main()
