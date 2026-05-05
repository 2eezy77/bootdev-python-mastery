''' Testing whether animal is dog, requiring both to be True: 4 legs, and less than 200kg'''
def is_dog(num_legs, weight):
    return num_legs == 4 and weight < 200


def main():
    tutus_leg_count = 4
    tutus_weight_kg = 185

    testing_if_dog = is_dog(tutus_leg_count, tutus_weight_kg)
    print(testing_if_dog)

main()