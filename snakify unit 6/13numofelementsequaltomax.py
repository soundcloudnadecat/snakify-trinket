max = 0
max_num = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max, max_num = element, 1
    elif element == max:
        max_num += 1
print(max_num)