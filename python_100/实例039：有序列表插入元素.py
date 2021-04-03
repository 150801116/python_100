#题目 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
list = [13,8,5,1]
print("请输入一个数：",end="")
num = int(input())
print("插入前")
print(list)
for i in range(len(list)):
    if (list[i]<=num)and(num<=list[i+1]):
        list.insert(i+1,num)       #通过insert插入，后续的会自动移位
        break
    elif (list[i]>=num)and(num>=list[i+1]):
        list.insert(i+1,num)
        break
print("插入后")
print(list)