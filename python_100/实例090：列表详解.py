#题目 列表使用实例。
list = [10086,'中国移动',[1,2,4,5]]

#访问列表长度
print(len(list))
#输出从第2位到列表结尾
print(list[1:])
#向列表里面添加元素
list.append('jack')

print(list)
#输出列表的最后一个元素
print(list[-1:])