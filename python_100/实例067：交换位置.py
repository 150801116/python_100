#题目 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
list = [15,2,3,4,53,23,41,4]
max=min=list[0]
for i in range(len(list)):
    if list[i]>max:
        max = list[i]
    if list[i]<min:
        min = list[i]
for i in range(len(list)):
    if list[i]==max:
        list[0],list[i]=list[i],list[0]
    elif list[i]==min:
        list[-1],list[i]=list[i],list[-1]
print(max,min)
print(list)