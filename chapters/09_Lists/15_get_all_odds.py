def get_odd(num):
    all_odds = []

    for i in range(0, num):
        if i % 2 != 0:
            all_odds.append(i)
        else:
            continue
    return all_odds


def test():
    twenty = 20
    thirty = 30
    fourty_five = 45
    extract_odd_numbers = get_odd(twenty)
    extract_odd_numbers1 = get_odd(thirty)
    extract_odd_numbers2 = get_odd(fourty_five)
    print(f"{extract_odd_numbers},\n{extract_odd_numbers1},\n{extract_odd_numbers2}")


def main():

    test()


main()
