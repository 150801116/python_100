#题目 计算两个矩阵相加。

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):  #内存行数及列数，可以用len(X[0])表示
        res[i][j] = X[i][j]+Y[i][j]
print(res)
