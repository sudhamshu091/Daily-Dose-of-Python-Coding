set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9}
intersection = set1.intersection(set2)
for i in intersection:
    set1.remove(i)
print(set1)
