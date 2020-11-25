def chinese_puzzle(num,numtires):
    ns='No solutions!'
    for i in range(num+1):
        j = num-i
        if 3*i+4*j==numtires:
            return i,j
    return ns,ns

num=35
numtires=125
print(chinese_puzzle(num,numtires))
