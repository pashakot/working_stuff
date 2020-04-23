def super_fibonacci(n, m):
    x = [0]
    if m > 0:
        for i in range(m):
            x.append(1)
    else:
        x.append(1)
    if n > m:
        while len(x) != n + 1:
            a = 0
            for i in range(m):
                a += x[len(x) - 1 - i]
            x.append(a)
        return x
    else:
        return x[n-1]


print(super_fibonacci(5, 3))
'''
    if n>m:
        z = n
        for i in range(m, n+1):
            fib_prev = x[i-1]
            fib_curr = x[i]
            fib_new = fib_prev+fib_curr
            x.append(fib_new)
    print(x[n])
    print(x)
'''
'''
    fib_prev = x[0]
    fib_curr = x[1]
    if n == 0:
        print(fib_prev)
    else:
        if n == 1:
            print(fib_curr)
        else:
            for i in range(n-1):
                fib_new
'''
