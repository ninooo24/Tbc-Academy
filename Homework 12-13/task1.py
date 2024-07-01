def format_string(string):
    formatted_string = string[-1] + string[:-1]
    return formatted_string


def main():
    user_input = input("Input: ")
    for i in range(len(user_input)):
        new_string = format_string(user_input)
        print(new_string)
        user_input = new_string


if __name__ == "__main__":
    main()

