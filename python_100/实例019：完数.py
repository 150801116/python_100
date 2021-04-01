#题目 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#看完题目心得，这个题目好麻烦！
#因子是不重复的！找出所有因子，再求和
import math
def findFactor(n):
    if n<0:
        return
    #考虑到因子是要求完全不重合的可以直接定义成集合
    res = {1}
    #res=set()
    #res.add(1)
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            res.add(i)
            res.add(int(n/i)) #前期都把这个因子忘记了
    return res

for i in range(2,1000):
    if(sum(findFactor(i))==i):
        print(i)


#参考答案 参考答案输出6，28，296
# def factor(num):
#     target=int(num)
#     res=set()
#     for i in range(1,num):
#         if num%i==0:
#             res.add(i)
#             res.add(num/i)
#     return res
#
# for i in range(2,1001):
#     if i==sum(factor(i))-i:
#         print(i)