def max_num(nums):
    negative_inf = float("-inf")

    for num in nums:
        if num > negative_inf:
            negative_inf = num
        elif nums is None:
            return negative_inf
    return negative_inf


def test():
    test_of_nums = max_num([1, 2, 3])
    print(test_of_nums)


def main():
    test()


main()
