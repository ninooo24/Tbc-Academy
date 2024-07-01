def to_upper(list):
    upper_case_list = []
    for item in list:
        upper_case_list.append(item.upper())
    return upper_case_list


def remove_short_strings(list):
    new_list = []
    for item in list:
        if len(item) >= 3:
            new_list.append(item)
    return new_list


def main():
    random_strings = ["python", "or", "List", "tbc", "academy"]
    print("List before: ", random_strings)
    random_short_strings = remove_short_strings(random_strings)
    print("List after:", to_upper(random_short_strings))


if __name__ == "__main__":
    main()
