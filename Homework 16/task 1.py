def average_temperature(temperatures):
    total = sum(temperatures)
    count = len(temperatures)
    average = total / count
    return average


def main():
    temperatures = [22, 25, 19, 23, 25, 26, 23]
    average_temp = average_temperature(temperatures)
    print(f"average temperature is {average_temp}")


if __name__ == "__main__":
    main()
