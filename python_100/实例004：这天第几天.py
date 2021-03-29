#题目 输入某年某月某日，判断这一天是这一年的第几天？
#解题思路，首先要根据键盘输入进行切割保存数据，其次要区分是否是闰年
#闰年条件（能被4整除且不能被100整除）OR（能被400整除）
print("请输入输入某年某月某日：",end="")
list = input()
Year = list.split("年")    #Year=['2020', '3月29日']
year = int(Year[0])    #注意需要强制转换一下，否则切割出来还是str型
Month = Year[1].split("月")  #Month=['3', '29日']
month = int(Month[0])
Day = Month[1].split("日")  #Day=['29', '']
day = int(Day[0])
temp = 0
# print(year)
# print(month)
# print(day)
list1=[31,28,31,30,31,30,31,31,30,31,30,31]  #平年2月是28天，闰年29天
if (year%4==0)and(year%100!=0):
    list1[1]=29
elif year%400==0:
    list1[1] = 29
for i in range(month-1):   #注意下标是从0开始的，月份是从1开始的
    temp +=list1[i]
temp +=day
# print(list,end="")
# print("是这一年的第",end="")
# print(temp,end="")
# print("天")
print(list+"是这一年的第"+"%d天"%temp)



