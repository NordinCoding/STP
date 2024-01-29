def main():
    number = 8
    new_number = division(number)
    print(multiplication(new_number))


def division(number):
    return int(number / 2)


def multiplication(number):
    return number * 4


main()
