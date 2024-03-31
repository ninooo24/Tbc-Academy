from task1 import format_string


def is_transformable(str_a, str_b):
    for i in range(len(str_a)):
        transformed_str = format_string(str_a[i:] + str_a[:i])
        if transformed_str == str_b:
            return "YES"
    return "NO"


def main():
    str_a = input("Input a: ")
    str_b = input("Input b: ")
    result = is_transformable(str_a, str_b)
    print("Output:", result)


if __name__ == "__main__":
    main()

