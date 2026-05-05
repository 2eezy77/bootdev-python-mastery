def convertBinary(guessOne, guessTwo, guessThree):
    guessOne = int(guessOne, 2)
    guessTwo = int(guessTwo, 2)
    guessThree = int(guessThree, 2)
    return guessOne, guessTwo, guessThree


def main():
    guessOne = '1100'
    guessTwo = '1011'
    guessThree = '0011'

    convertMyBinaries = convertBinary(guessOne, guessTwo, guessThree)
    print(convertMyBinaries)

main()


