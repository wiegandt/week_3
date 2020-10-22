a = int(input("number: "))
b = int(input("number: "))
c = int(input("number: "))
d = int(input("number: "))
e = int(input("number: "))


def Average(lst):
    return sum(lst) / len(lst)

lst = [a, b, c, d, e]
average = Average(lst)

print("Average: ", round(average, 2))

print("Sum: ", sum(lst))