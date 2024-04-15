import random


def int_len(i):
    return len(str(i))


def main():
    my_list = []
    for _ in range(100):
        my_list.append(random.randint(10, 1000000000))

    print(my_list)
    min_num = min(my_list, key=int_len)
    max_num = max(my_list, key=int_len)
    print("Minimum number is ", min_num)
    print("Maximum number is ", max_num)
    sorted_list = sorted(my_list, key=int_len)
    print("Sort ascending: ", sorted_list)
    sorted_list = sorted(my_list, key=int_len, reverse=True)
    print("Sort descending: ", sorted_list)


if __name__ == '__main__':
    main()

