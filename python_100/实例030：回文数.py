#题目 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
print("请输入一个5位数：",end="")
n = input()
len = len(n)
mid = int(len/2)
flag = 0  #作为一个标签
for i in range(mid):
    if n[i]!=n[len-i-1]:
        print(n, "不是回文序列")
        flag =1
        break
if flag==0:
    print(n, "是回文序列")




