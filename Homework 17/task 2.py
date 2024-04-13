import random


def main():
    list_1 = []
    list_2 = []
    list_3 = []
    for _ in range(10):
        list_1.append(random.randrange(1, 10))
        list_2.append(random.randrange(1, 10))
        list_3.append(random.randrange(1, 10))

    sum = map(lambda x, y, z: x + y + z, list_1, list_2, list_3)

    print(f"list1 - {list_1}")
    print(f"list2 - {list_2}")
    print(f"list3 - {list_3}")
    print(f"Sum   - {list(sum)}")


if __name__ == "__main__":
    main()
