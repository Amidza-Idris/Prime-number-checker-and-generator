# prime number generator and checker

def choose():
    print(end="\n")
    choice = input("generate or check number/s (c/g): ")

    if choice == "c" or choice == "C":
        check()
    elif choice == "g" or choice == "G":
        gen()
    else:
        print("You are a moron, use me bitch!")


def check():
    num = int(input("Number to check: "))
    print(end="\n")
    flag = False

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:

                flag = True
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
    choose()


def gen():
    print("Enter the area of numbers to check:")
    first = int(input("From: "))
    second = int(input("To: "))
    print(end="\n")

    for a in range(first, second + 1):
        count = 0
        for i in range(2, (a // 2 + 1)):
            if a % i == 0:
                count = count + 1
                break

        if count == 0 and a != 1:
            print(a, end="  ")
            # New thing I learned is print has different functions within itself
            # For example print("G", "F" sep="" , end="\n")
            # sep="" separates (or in this case keeps them together) chars in print statement
            # end="" ends the line with "", if the case is end="\n", the next text will be in a new line
    print(end="\n")
    choose()


choose()
