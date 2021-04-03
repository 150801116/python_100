#题目 使用lambda来创建匿名函数。
#我好像没见过匿名函数，又是菜鸡的一天，那就捡起来！
#参考答案
Max = lambda x,y:x*(x>=y)+y*(y>x)
Min = lambda x,y:x*(x<=y)+y*(y<x)
print("请输入a:",end="")
a = int(input())
print("请输入b:",end="")
b = int(input())
print("Max:",end="")
print(Max(a,b))
print("Min:",end="")
print(Min(a,b))