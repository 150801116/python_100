#题目 输入3个数a,b,c，按大小顺序输出。
print("请输入a:",end="")
a = int(input())
print("请输入b:",end="")
b = int(input())
print("请输入c:",end="")
c = int(input())
print("将a,b,c按从小到大的顺序输出：",end="")
if a>b:
    a,b=b,a
    if a>c:
        a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)