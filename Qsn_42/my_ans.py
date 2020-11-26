def chinese_puzzle(num,numtires):
    r = num*4 - numtires
    c = num - r
    return r,c
print(chinese_puzzle(34,134))

