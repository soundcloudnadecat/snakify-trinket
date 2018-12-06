a = input()
if len(a) < 2:
    print("Empty String")
else:
    print(a[:2] + a[len(a) - 2] + a[len(a) - 1])