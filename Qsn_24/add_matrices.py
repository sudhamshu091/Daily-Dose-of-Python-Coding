x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[12,11,12],[13,14,15]]
result = [[0,0,0],[0,0,0],[0,0,0]]

if len(x) != len(x[0]):
    print("Error! Inner dimentions donot agree")
else:
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    for k in result:
        print(k)
