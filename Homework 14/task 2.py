from task1 import gcd_iterative, gcd_recursive


def lcm(a, b):
    return (a * b) // gcd_iterative(a, b), (a * b) // gcd_recursive(a, b)


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    lcm_iterative, lcm_recursive = lcm(a, b)

    print(f"LCM of {a} and {b} using iterative GCD is {lcm_iterative}.")
    print(f"LCM of {a} and {b} using recursive GCD is {lcm_recursive}.")


if __name__ == "__main__":
    main()

