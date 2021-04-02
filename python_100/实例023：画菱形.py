#题目 打印出如下图案（菱形）:
 #    *
 #   ***
 #  *****
 # *******
 #  *****
 #   ***
 #    *
#非递归方法
n = 7
t=n//2
for i in range(t+1):
    print(" "*(t-i),end="")
    print("*"*(2*i+1))
for j in range(t):
    print(" "*(j+1),end="")
    print("*"*((t-j)*2-1))

#函数算法
def show(n):
    middle_= int(n/2)
    res = [n]   #用于存放每一行*个数
    # print("------")
    # print(res)  #[7]
    # print("------")
    while n>1:
        n-=2
        res.insert(0,n) #前插入(n-2)
        res.append(n)   #后插入(n-2)
    print(res)

    for one in res:
        print(" "*(middle_-int(one/2))+"*"*one)
n = 7
show(n)




