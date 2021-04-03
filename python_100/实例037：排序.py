#题目 对10个数进行排序。
list = [1,23,14,29,19,25,29,30,9,11]
print("排序前：",end="")
print(list)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print("排序后：",end="")
print(list)