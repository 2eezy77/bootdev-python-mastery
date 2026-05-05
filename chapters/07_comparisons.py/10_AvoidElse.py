def rental(rent_equip, time_rented):
    if rent_equip >= time_rented:
        return "time exceeded, charge late fee"
    return "no fee"


def main():
    snowboard_rented = 10
    time_with_equipment = 8

    time_with_rentals = rental(snowboard_rented, time_with_equipment)
    print(time_with_rentals)

main()

