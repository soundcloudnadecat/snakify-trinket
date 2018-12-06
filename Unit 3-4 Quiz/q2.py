a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print("YES")
else:
    print("NO")

if a > b > c:
    print(c, b, a)
elif a > b and a > c and b < c:
    print(b, c, a)
elif a < b and a > c and b > c:
    print(c, a, b)
else:
    if b < a and a < c:
        print(b, a, c)