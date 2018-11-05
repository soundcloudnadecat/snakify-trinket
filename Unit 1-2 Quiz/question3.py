number = int(input("Two (2) digit number: "))
tens = (number // 10) % 10
ones = number % 10
swap = str(ones) + str(tens)
print(swap)