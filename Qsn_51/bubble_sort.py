a = [1,7,6,5,4,3,2,10]
for j in range(len(a)):
    i = 0
    while i < len(a) - 1:
        if a[i] > a[i + 1]:
            a[i],a[i + 1] = a[i + 1],a[i]
        i = i + 1
print(a)
