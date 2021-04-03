#题目 求输入数字的平方，如果平方运算后小于 50 则退出。
import math
flag=0
while flag==0:
    print("请输入一个数字：",end="")
    n = int(input())
    res = math.pow(n,2)
    if res<50:
        flag=1