while True:

    number = int(input("Enter a number:  "))


    if number < 0:
        print("Negative number is not allowed")
        continue

    if number == 0:
        print("The program is stopped")
        break

    square = number ** 2
    print("The square root =", square)