#题目 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
print("请输入一个不多于5位的正整数：",end="")
n = input()
len = len(n)
print(n,"是",len,"位数")
for i in range(len-1,-1,-1):
    print(n[i],end="")
#print(n[::-1])  #可以直接逆序输出