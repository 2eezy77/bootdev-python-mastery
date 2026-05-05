car_height = 7
garage = 6

def willItFit(car, garage):
    return car <= garage

test_size = willItFit(car_height, garage)
print(test_size)