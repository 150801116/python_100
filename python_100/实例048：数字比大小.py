#题目 数字比较。
print("请输入X=",end="")
x = int(input())
print("请输入Y=",end="")
y = int(input())
if x<y:
    print("x小于y")
elif y<x:
    print("y小于x")
else:
    print("x等于y")