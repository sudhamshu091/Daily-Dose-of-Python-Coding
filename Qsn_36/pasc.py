def pascal(n):
    if n==0:
        return [1]
    else:
        N = pascal(n-1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]
def pascal_triangle(n):
    for i in range(n):
        print(pascal(i))
print(pascal_triangle(20))
