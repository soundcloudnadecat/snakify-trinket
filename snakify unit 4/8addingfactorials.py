a = int(input())
pf = 1
ps = 0
for i in range(1, a + 1):
    pf *= i
    ps += pf
print(ps)