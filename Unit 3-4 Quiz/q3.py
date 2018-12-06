a = int(input("MUST BE A FOUR (4) DIGIT NUMBER"))

ones = a % 10
tens = a // 10 % 10
hundreds = a // 100 % 10
thousands = a // 1000

if ones == thousands and tens == hundreds:
    print("YES")
else:
    print("NO")