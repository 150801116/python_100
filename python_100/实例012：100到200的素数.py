#题目 判断101-200之间有多少个素数，并输出所有素数。
#素数的定义，只有1和本身两个质数，
import math
count = 0
for i in range(100,200):
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            break
        elif j==int(math.sqrt(i)):
            count +=1
            print(i)
print("101-200之间一共有",count,"个素数")

#参考答案
import math
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            flag=1
            break
    if flag:
        continue
    print(i)


print('\nSimplify the code with "else"\n')


for i in range(100,200):
    for j in range(2,round(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        print(i)    #else与for联用，只有在内在循环完全遍历结束之后才会调用else