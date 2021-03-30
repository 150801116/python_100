#题目 将一个列表的数据复制到另一个列表中。
import copy
list1 = [1,2,3,4,5]
list2=[]
for i in range(len(list1)):
    list2.append(list1[i])
print(list2)


a=[1,2,3,4,['a','b']]
b=a   #赋值,即b和a指向同一个地址，引用对象
c=a[:] #浅拷贝，深拷贝父对象（一级目录），即5不随着增加，子对象（二级目录）不拷贝，子对象是引用，即c随着增加
d=copy.copy(a) #浅拷贝，深拷贝父对象（一级目录），即5不随着增加，子对象（二级目录）不拷贝，子对象是引用，即c随着增加
e=copy.deepcopy(a) #深拷贝，e不跟随a的变化而变化，两个地址

a.append(5)
a[4].append('c')
print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print("e=",e)

