import random


def generate_list():
    return [random.randint(1, 30) for _ in range(50)]


def remove_duplicates(input_list):
    my_list = []
    for num in input_list:
        if num not in my_list:
            my_list.append(num)
    print("list before: ", input_list)
    return my_list


def main():
    original_list = generate_list()
    unique_list = remove_duplicates(original_list)
    print("List -", unique_list)
    print("Length -", len(unique_list))


if __name__ == "__main__":
    main()

