from os import system
import types


def convert(num, base):
    pass


def validate(num, base):
    assert isinstance(num, str), "num must be of type str"
    assert isinstance(base, int), "base must be of type int"
    validNumbers = "0123456789abcdef"

    for i in range(len(num)):
        if num[i] not in validNumbers.lower()[:base]:
            return False

    return True


def main():
    # ask user for base (int[2, 16])

    print("What base is your number?")
    base = int(input(">>> "))

    print("What is your number?")
    number = str(input(">>> "))

    print(validate(number, base))
    print(base, number)

    return None


if __name__ == '__main__':
    main()
    exit()
