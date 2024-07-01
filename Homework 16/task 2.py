import random


def generate_list():
    random_numbers = [random.randint(1, 30) for _ in range(50)]
    return random_numbers


def manipulate_list(input_list):
    output_list = []
    for number in input_list:
        output_list.extend([number] * number)
    return output_list


def main():
    random_numbers = generate_list()
    print("old list:", random_numbers)
    manipulated_list = manipulate_list(random_numbers)
    print("new list:", manipulated_list)
    print("length:", len(manipulated_list))


if __name__ == "__main__":
    main()
