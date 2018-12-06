max_1 = int(input())
max_2 = int(input())
if max_1 < max_2:
    max_1, max_2 = max_2, max_1
element = int(input())
while element != 0:
    if element > max_1:
        max_2, max_1 = max_1, element
    elif element > max_2:
        max_2 = element
    element = int(input())
print(max_2)