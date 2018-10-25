number = int(input())
ones = number % 10
tens = number // 10 % 10
hundreds = number // 100
print(ones + tens + hundreds)