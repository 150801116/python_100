#题目 利用递归方法求5!。
def factorial(n):
    if n<2:
        return 1
    return factorial(n-1)*n
n = 5
print("5!=",factorial(n))

