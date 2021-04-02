#题目 按相反的顺序输出列表的值。
list = ['a','b','c','d','e']
#print(list[::-1])  #可以直接调用函数输出
for i in range(len(list)-1,-1,-1):
    print(list[i],end="")