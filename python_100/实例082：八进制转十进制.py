#题目 八进制转换为十进制
import math
print("请输入一个八进制数：",end='')
n = input()
res = 0
for i in range(len(n)):
    res += int(n[i])*math.pow(8,len(n)-i-1)
print(res)