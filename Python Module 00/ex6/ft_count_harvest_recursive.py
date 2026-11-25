def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))

    def recursive_count(days):
        if days >= 1:
            recursive_count(days - 1)
            print(f"Day {days}")

    recursive_count(days_until_harvest)
    print("Harvest time!")
