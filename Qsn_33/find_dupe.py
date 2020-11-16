def find_dupe(num):
    list = []
    for i in range(len(num)):
        if num[i] in list:
            return num[i]
        else:
            list.append(num[i])
    return -1
print(find_dupe([2,3,3,4]))
