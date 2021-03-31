#题目 将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#再一次感慨list真的很香，个人认为等价于可变长数组
#看到参考答案，发现整数不一定是正的，不由的发出感慨，秒呀，程序员大哥的全面性思维我还差很多
import math
# def isPrime(n):   #写到一半发现压根不用判断，因为所有的非质数都会被拆解成更小的数相乘
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             break
#             return 0
#     else:
#         return 1
def findFactor(n):
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            #print(i)
            # if(isPrime(i)==1):
           list.append(i)
           return findFactor(int(n/i))
    else:
        #print(n)
        list.append(n)
        return n

print("请输入一个整数：",end="")
n = int(input())
list=[]
#print(list)
print(n,"=",end="")
if(n<0):    #用于负数情况！！
    print("-1*",end="")
    n=abs(n)   #求绝对值！
findFactor(n)
for i in range(len(list)):
    if i==len(list)-1:
        print(list[i])
    else:
        print(list[i],"*",end="")


#参考答案
target=int(input('输入一个整数：'))
print(target,'= ',end='')

if target<0:
    target=abs(target)
    print('-1*',end='')

flag=0
if target<=1:
    print(target)
    flag=1


while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break  #这个break用于控制结束的就是找全了，跳转到if flag 那一行开始，且flag值为1后可以跳出while
            print('*',end='')
            target/=i
            break     #这个break用户控制开始寻找下一个数字，跳转到if flag 那一行开始
