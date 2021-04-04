#题目 打印出杨辉三角形前十行。
#杨辉三角：
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1
import numpy
# def show(n):
#
#     A = []
#     for i in range(n):   #二维数组定义
#         A.append([])
#         for j in range(n):
#             A[i].append(0)
#
#     for i in range(n):
#         A[i][0] = 1
#         A[i][i] = 1
#     # for i in range(n):
#     #     for j in range(i+1):
#     #         print(A[i][j],end=" ")
#     #     print()
#     for i in range(2,n):
#         for j in range(1,i):
#            A[i][j]=A[i-1][j-1] + A[i-1][j]
#     #print("--------")
#     for i in range(n):
#         for j in range(i+1):
#             print(A[i][j],end=" ")
#         print()
#     #print(A)
# show(10)
#下面的这种方法
#B = [[0]*10]*10#这种赋值方式是不对的，[0]*10是浅拷贝，实则是一个地址
#使用list创建二维数组可以列表生成式法：A=[[0 for i in range(n)]for j in range(m)] n行，m列

B=[[0 for i in range(10)]for j in range(10)]
for i in range(10):
    for j in range(10):
        print(B[i][j],end=" ")
    print()
print("=======")
for i in range(10):
    B[i][0]=1
    B[i][i]=1
for i in range(10):
    for j in range(i+1):
        print(B[i][j],end=" ")
    print()
