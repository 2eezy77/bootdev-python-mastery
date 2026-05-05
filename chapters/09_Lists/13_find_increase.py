def check_levels():
    old_levels = [1, 2, 2, 3, 3]
    new_levels = [1, 2, 3, 4, 5]

    for i in range(0, len(old_levels)):
        if old_levels[i] < new_levels[i]:
            print(i)
        else:
            continue


def test():
    check_levels()


def main():
    test()


main()
