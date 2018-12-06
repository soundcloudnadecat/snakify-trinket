a = input()
b = a[0]
if a.count(b) > 1:
    newstring = a.replace(b, '$')
    print(b + newstring[1:])
else:
    print("Only one instance of the first character.")