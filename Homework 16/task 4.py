def merge_list(list1, list2):
    merged_list = list1 + list2
    length = len(merged_list)

    for i in range(length):
        minimal = i
        for j in range(i + 1, length):
            if merged_list[j] < merged_list[minimal]:
                minimal = j
        merged_list[i], merged_list[minimal] = merged_list[minimal], merged_list[i]

    return merged_list


def main():
    list1 = [15, 5, 58, 8, 125]
    list2 = [78, 25, 63, 88, 267]
    print("example 1")
    print(list1)
    print(list2)
    print("merge list is, ", merge_list(list1, list2))
    list3 = [71, 25, 98, 612]
    list4 = [32, 2, 10, 3, 257]
    print("---------------------------------------------------------------------------")
    print("example 2")
    print(list3)
    print(list4)
    print("merge list is, ", merge_list(list3, list4))


if __name__ == "__main__":
    main()
