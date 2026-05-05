def pop_items(list):
    for item in range(0, len(list)):
        pop_description = list.pop()
        print(f"first grab: {pop_description}")


def main():
    car_description = [
        "Toyota",
        "Camry",
        "xse"
    ]

    describe_car_backwards = pop_items(car_description)
main()


