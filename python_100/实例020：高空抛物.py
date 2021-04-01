#题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
import math
total=100 #球下落高度
n = 10   #n表示第几次落地
sum = 0     #sum总共经过多少米,前(n-1)的下落去反弹总和
height = 0  #第n次落地后的，反弹距离
height = total*math.pow(1/2,n)
print("第",n,"次落地后反弹",height,"米")
height_temp=total
sum=height_temp
for i in range(1,n):
    height_temp=height_temp/2
    sum +=height_temp*2
print("第",n,"次落地时，总经过",sum,"米")

#参考答案
high=200.
total=100
for i in range(10):
    high/=2
    total+=high
    print(high/2)
print('总长：',total)


