dic = {}
s=input("Enter the input string:")
for i in s:
    dic[i] = dic.get(i,0)+1
print('\n'.join(['%s,%s with Probability :%s' % (k, v, v/len(s)) for k, v in dic.items()]))
