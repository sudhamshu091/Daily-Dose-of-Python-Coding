list = [11,23,34,56,12,11,45,23,11]
dict = {}
for i in list:
    if (i in dict):
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
