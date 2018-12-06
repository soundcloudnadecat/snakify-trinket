a = int(input())
cards = 0
for i in range(1, a + 1):
    cards += i

for i in range(a - 1):
    cards -= int(input())
print(cards)