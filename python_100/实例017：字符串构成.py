#题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#让我以最热烈的掌声欢迎ord（)输出的是字符串的ascii码值，输出为整型
print("请输入一行字符串：",end="")
str = input()
x1=x2=x3=x4=0 #x1,x2,x3,x4分别表示英文字母、空格、数字和其它字符的个数
# print(ord(str[0]))
# print(type(ord(str[0])))
for i in range(len(str)):
    if ((ord(str[i])>=65)and(ord(str[i])<=90))or((ord(str[i])>=97)and(ord(str[i])<=122)):
        x1+=1
    elif ord(str[i])==32:
        x2+=1
    elif (ord(str[i])>=48)and(ord(str[i])<=57):
        x3+=1
    else:
        x4+=1
print("英文字母个数：",x1)
print("空格个数：",x2)
print("数字个数：",x3)
print("其他个数：",x4)

#参考答案
#很明显我又孤陋寡闻了内置函数都这么强大了，isspace(),isdigit(),isalpha()
string=input("输入字符串：")
alp=0
num=0
spa=0
oth=0
for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isdigit():
        num+=1
    elif string[i].isalpha():
        alp+=1
    else:
        oth+=1
print('space: ',spa)
print('digit: ',num)
print('alpha: ',alp)
print('other: ',oth)
