def reversedigit(n):
    while (n > 0):
        digit = n % 10
        n = n // 10
        print(digit, end = " ")
reversedigit(64884758)
