max = 0
index = -1
element = -1
length = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index = length
    length += 1
print(index)