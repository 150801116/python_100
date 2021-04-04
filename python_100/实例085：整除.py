#题目 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
print("请输入一个奇数：")
n = int(input())
for i in range(1,10000):
    list = ['9'*i]
    #print(list)
    t = int(list[0])
    #print(t)
    if t%n==0:
        s = str(t)
        print("最少需要",len(s),"个9才能整除",n)
        print("%d/%d=%d"%(t,n,t/n))
        break