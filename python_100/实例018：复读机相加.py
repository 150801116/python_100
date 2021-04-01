#题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
import math
print("请设置几个数相加：")
n = int(input())
print("请设置相加的数：")
a = int(input())
sum = 0
n_temp = n
for i in range(1,n+1):
    sum += i*a*math.pow(10,n_temp-1)
    n_temp -= 1
print("总和为：",sum)

#参考答案
#一个字，秒，很简洁！
a=input('被加数字：')
n=int(input('加几次？：'))
res=0
for i in range(n):
    res+=int(a) #直接强制转换，str变为int
    a+=a[0] #直接字符串增加一位
print('结果是：',res)