word=input('enter:')
total=len(word)
dict={}
for i in word:
    dict[i]=dict.get(i,0)+1
for key,value in dict.items():
    print(key,value,'with Probability:')
    print(value/total)
