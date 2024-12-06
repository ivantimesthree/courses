def gather_temperature_for_days(days):
    list_of_temperatures = []
    for i in range(days):
        current_day_temp = int(input(f"Day {i + 1}'s high temp: "))
        list_of_temperatures.append(current_day_temp)
    return list_of_temperatures


def calculate_average_temp(temp_for_each_day, days):
    average_temp = sum(temp_for_each_day) / days
    print(f"Average temperature: {average_temp:.2f}")
    return average_temp


def calculate_days_above_average(average_temp, temp_for_each_day):
    days_above_average = [x for x in temp_for_each_day if x > average_temp]
    print(f"Day(s) above average: {len(days_above_average)}")
    return days_above_average


def main():
    days = int(input("How many days temperature? "))
    temp_for_each_day = gather_temperature_for_days(days)
    average_temp = calculate_average_temp(temp_for_each_day, days)
    days_above_average = calculate_days_above_average(average_temp, temp_for_each_day)


if __name__ == "__main__":
    main()
