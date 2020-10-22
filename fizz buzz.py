for x in range(1, 101):
    if (x % 3) == 0:
        x = "fizz"
    elif (x % 5) == 0:
        x = "buzz"
    elif (x % 3) == 0 and (x % 5) ==0:
        x = "fizzbuzz"

    print(x)