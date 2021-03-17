x = "a"
y = "b"
print(x)
print(y)
print("不换行-----")
print (x,end="")
print (y,end="")
print()
s="abcdef" #字符串
print(s[1:5]) #取头不取尾
print(s[-5:-1])
#挑着截取
letters=["c","h","e","c","k","i","o"] #列表
print(letters[1:4:2])
tuple=(123,"john")#元组
print(tuple*2)
dict = {}#字典
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict ) # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

#集合
sites = {"Google","Taobao","Runoob","Facebook","Zhihu","Baidu"}
print(sites)
a = set("abracadabra")
b = set("alacazam")
print(a-b) #a,b差集
print(a|b) #a,b并集
print(a&b) #a,b交集
print(a^b) #a,b中不同时存在的元素

#总结字符串，列表，元组，字典的区别
#字符串：不可修改，其他等价于列表处理
#列表：可重复，类型可不同，可动态增删改查
#元组：元组相对于列素后面加逗号“,”，否则创建的不是一个元组，而是一个字符串。
      #tuple=("a",) string=("a")表结构上区别不搭，但是元组是只读不可修改，且元组在定义的时候长度和内容都是固定的！
      #若想创建包含一个元素的元组，则必须在该元
#字典：列表是有序的对象，字典是无序的对象，两者区别是，字典中元素通过键存取，而不是通过偏移存取
      #字典由索引（key）和它对应的值(value)组成
#不可变数据（3个）：数字，字符串，元组
#可变数据（3个）：列表，字典，集合
