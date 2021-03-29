#题目 输入三个整数x,y,z，请把这三个数由小到大输出。
print("请输入三个整数：",end="")
str = input();
x=int(str.split(",")[0])
y=int(str.split(",")[1])
z=int(str.split(",")[2])
# print(x)
# print(y)
# print(z)
# print(min(x,y,z),end=",")
# print(x+y+z-min(x,y,z)-max(x,y,z),end=",")
# print(max(x,y,z))
#不调用函数方法
# if x>y:
#     x=x+y
#     y=x-y
#     x=x-y
# if x>z:
#     x=x+z
#     z=x-z
#     x=x-z
# if y>z:
#     y=y+z
#     z=y-z
#     y=y-z
# print(x,y,z)

#直接调用sort函数
list=[x,y,z]
print(list)
list.sort()
print(list)