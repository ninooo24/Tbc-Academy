def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    gcd_iter = gcd_iterative(a, b)
    print(f"GCD of {a} and {b} is {gcd_iter}.")

    gcd_rec = gcd_recursive(a, b)
    print(f"GCD of {a} and {b} is {gcd_rec}.")


if __name__ == "__main__":
    main()
