#题目 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#首先百度一下周一到周日的英文：Monday，Tuesday,Wednesday，Thursday,Friday,Saturday,Sunday
print("请输入星期几的第一个字母（区分大小写）：",end="")
str = input()
if str =="M":
    print("Monday")
elif str == "W":
    print("Wednesday")
elif str == "F":
    print("Friday")
elif str =="T":
    print("请输入星期几的第二个字母（区分大小写）：", end="")
    str2 = input()
    if str2 =="u":
        print("Tuesday")
    elif str2 =="h":
        print("Thursday")
elif str[0] =="S":
    print("请输入星期几的第二个字母（区分大小写）：", end="")
    str2 = input()
    if str2 == "a":
        print("Saturday")
    elif str2 == "u":
        print("Sunday")

#参考答案,很明显答案用字典显得更简洁！
weekT={'h':'thursday',
       'u':'tuesday'}
weekS={'a':'saturday',
       'u':'sunday'}
week={'t':weekT,
      's':weekS,
      'm':'monday',
      'w':'wensday',
      'f':'friday'}
a=week[str(input('请输入第一位字母:')).lower()]
if a==weekT or a==weekS:
    print(a[str(input('请输入第二位字母:')).lower()])
else:
    print(a)