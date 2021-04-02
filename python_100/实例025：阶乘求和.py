#题目 求1+2!+3!+…+20!的和。
#递归算法
def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
sum = 0
for i in range(1,21):
    sum +=factorial(i)
print("总和为",sum)

#参考答案，牛逼呀，没有递归，则计算量降低好多,记住他！
#程序分析 1+2!+3!+…+20!=1+2(1+3(1+4(…20(1))))
res=1
for i in range(20,1,-1):
    res=i*res+1
print(res)