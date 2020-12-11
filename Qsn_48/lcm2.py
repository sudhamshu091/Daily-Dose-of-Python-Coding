def lcm2(n1,n2):
    if n1 > n2:
        n1, n2 = n2, n1
    for i in range(n2, n1*n2+1, n2):
        if i % n1 == 0:
            return i
