def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("30 celsius is ", celsius_to_fahrenheit(30), "fahrenheit")
    print("100 celsius is ", celsius_to_fahrenheit(100), "fahrenheit")
    print("212 fahrenheit is ", fahrenheit_to_celsius(212), "celsius")
    print("86 fahrenheit is ", fahrenheit_to_celsius(86), "celsius")


if __name__ == "__main__":
    main()
