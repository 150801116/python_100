#题目 求一个3*3矩阵主对角线元素之和。
mat =[[1,2,3],
     [3,4,5],
     [4,5,6]
    ]
sum = 0
for i in range(len(mat)):
    sum +=mat[i][i]
    print(mat[i][i])
print(sum)