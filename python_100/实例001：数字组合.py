#题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# list = [1,2,3,4]
# list1 = []
# for i in list:
#     for j in list:
#         if i!=j:
#             for k in list:
#                    if (k!=i):
#                        if(k!=j):
#                         temp = i*100+j*10+k
#                         list1.append(temp)
# print(list1)
# print(len(list1))

#太耗时了，三次循环！且需要占用list空间
# list = [1,2,3,4]
# count=0
# for i in list:
#     for j in list:
#             for k in list:
#                   if((i!=j)and(i!=k)and(j!=k)):
#                         #print(i,j,k)    #这种格式的输出中间有空格
#                         print("%d%d%d"%(i,j,k)) #这种格式的输出中间无空格
#                         count = count+1
#
# print(count)

#太耗时了，三次循环！
# count = 0
# for i in range(1,5):   #range(a,b)取a不取b
#     for j in range(1,5):
#         for k in range(1,5):
#             if((i!=j)and(i!=k)and(j!=k)):
#                 temp = i*100+j*10+k
#                 count = count +1
#                 print(temp)
# print(count)

#用itertools中的permutations
#permutations(a,r),从a中取出r个不同的元素，并进行排列组合,生成的是元组
# import itertools
# count = 0
# list = [1,2,3,4]
# for i in itertools.permutations(list,3):
#     print(i)
#     count +=1
# print(count)

#拓展如果是0，1，2，3这四位数生成三位数？
count = 0
for i in range(1,4):
    for j in range(0,4):
        for k in range(0,4):
            if (i!=j)and(i!=k)and(j!=k):
                print("%d%d%d"%(i,j,k))
                count +=1
print(count)

#总结，如果可以用内置函数则inertools最方便，否则则需要三次循环，且相对于从列表里面取数据，range更加灵活，且不占空间！