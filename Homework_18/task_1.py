def characteristics_for_temperatures(temps):
    result = []
    for day, daily_temp in enumerate(temps, start=1):
        avg_temp = sum(daily_temp) / len(daily_temp)
        max_temp = max(daily_temp)
        min_temp = min(daily_temp)
        result.append(f"Day {day}: Average Temp = {avg_temp}, Max Temp = {max_temp}, Min Temp = {min_temp}")
    return result


def avg_of_week(temps):
    daily_averages = [sum(daily_temp) / len(daily_temp) for daily_temp in temps]
    weekly_average = sum(daily_averages) / len(daily_averages)
    return weekly_average


def main():
    my_tuple = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

    temperature_characteristics = characteristics_for_temperatures(my_tuple)
    for temp_info in temperature_characteristics:
        print(temp_info)

    print("Average temperature for the week:", avg_of_week(my_tuple))


if __name__ == "__main__":
    main()
