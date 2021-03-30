#程序分析 斐波那契数列（Fibonacci sequence），从1,1开始，后面每一项等于前面两项之和。图方便就递归实现，图性能就用循环。
print("请输入n:",end="")
n = int(input())
#非递归算法
x1=1
x2=1
for i in range(n-2):  #减去2是因为剔除了，前面两个1，1的位置，算法复杂度O(n)
    temp=x1+x2
    x1=x2
    x2=temp
print(temp)

#递归算法,算法复杂度O(2^n)
def Fib(n):
    if n<=2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(n))