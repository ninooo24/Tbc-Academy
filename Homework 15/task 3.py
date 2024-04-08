def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]


def main():
    strings = ["TBC","Python","test"]
    for i in strings:
        reversed_string = reverse(i)
        print(f"Original: {i}, Reversed: {reversed_string}")


if __name__ == "__main__":
    main()


