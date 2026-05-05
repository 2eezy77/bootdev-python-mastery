def sum(a, b, c, d):
    total = a + b + c + d 
    return total

def average_number(a, b, c, d):
    average = (a + b + c + d ) / 4
    return average

def main():
    total_sum = sum(1,2,3,4)
    average_of_num = average_number(1,2,3,4)
    print(total_sum)
    print(average_of_num)
main()