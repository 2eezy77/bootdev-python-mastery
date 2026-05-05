def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total

last = 10 #0123456789
last1 = 5 #012345
last2 = 25 #0123456789 10 11 12 ...
only_odd = sum_of_odd_numbers(last2)
print(only_odd)
