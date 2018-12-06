a = int(input())
if a == 0:
    print(0)
else:
    prev_fib, next_fib = 0, 1
    n = 1
    while next_fib <= a:
        if next_fib == a:
            print(n)
            break
        prev_fib, next_fib = next_fib, prev_fib + next_fib
        n += 1
    else:
        print(-1)