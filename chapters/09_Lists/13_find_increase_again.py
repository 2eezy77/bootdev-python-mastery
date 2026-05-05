def check_level():
    old_level = [1, 3, 5, 8]
    new_level = [1, 5, 5, 8]

    for i in range(0, len(old_level)):
        if old_level[i] < new_level[i]:
            print(i)
        else:
            continue


def test():
    check_level()


def main():
    test()


main()
