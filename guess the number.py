n = 7
guess = int(input("guess the number: "))

if n < guess:
    print("The stored number is lower")
elif n > guess:
    print("The stored number is higher")
elif n == guess:
    print(" You found the number: ", n)