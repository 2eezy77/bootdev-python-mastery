def sum_game(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total

first = 0
last = 10

sumOfInputs = sum_game(first, last)
print(sumOfInputs)