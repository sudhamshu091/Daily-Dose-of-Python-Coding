def rgcd(x,y):
    a = max([x,y])
    b = min([x,y])
    if b == 0:
        return a
    else:
        return rgcd(b,(a % b))
print(rgcd(348,48))
print(rgcd(35,14))
