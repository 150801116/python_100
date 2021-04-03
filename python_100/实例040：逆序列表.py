#题目 将一个数组逆序输出
list = [1,2,3,4,5]
print("方法一")
for i in range(int(len(list))-1,-1,-1):
    print(list[i])
print("方法二")
print(list[::-1])
#参考答案
print("方法三")
list.reverse()
print(list)