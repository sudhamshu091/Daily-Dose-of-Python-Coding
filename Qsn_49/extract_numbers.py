import re
string = "[5, 2, 6, 5,], [7, 2, 8, 5,]"
temp = re.findall(r'\d+', string)
res = list(map(int, temp))
print(res)
