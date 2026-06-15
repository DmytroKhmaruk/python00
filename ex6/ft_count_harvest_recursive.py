def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def print_days(days):
        if days == 0:
            return
        print_days(days - 1)
        print("Day", days)

    print_days(days)
    print("Harvest time!")
