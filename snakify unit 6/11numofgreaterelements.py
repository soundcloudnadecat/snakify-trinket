previous = int(input())
answer = 0
while previous != 0:
    next = int(input())
    if next != 0 and previous < next:
        answer += 1
    previous = next
print(answer)