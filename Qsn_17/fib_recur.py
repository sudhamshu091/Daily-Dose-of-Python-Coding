def fib_rec(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        x = fib_rec(n-1)
        # the new element the sum of the last two elements
        x.append(sum(x[:-3:-1]))
        return x
x=fib_rec(5)
print(x)
