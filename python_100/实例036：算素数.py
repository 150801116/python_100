#题目 求100之内的素数。
#素数：只有1和它本身两个因数的自然数
import math
for i in range(1,100):
    flag = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i%j ==0:
            flag = 1
            break
    if flag == 0:
        print(i,end=" ")

#参考答案
lo=int(input('下限：'))
hi=int(input('上限：'))
for i in range(lo,hi+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)