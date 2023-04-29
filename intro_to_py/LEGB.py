def print_total():
    def inner_print_total():
        total = 7
        print(f"From inner function: {total=}")

    total = 12
    inner_print_total()
    print(f"From function: {total=}")

total = 5
print_total()
print(f"From global: {total=}")


