#题目 输出指定格式的日期。
#很明显这个题目又让我全新认识了一个模块datetime()
#strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定
import datetime
print(datetime.date.today()) #输出当天时间,格式为YYYY-MM-DD
print(datetime.date(2333,2,3)) #将2333，2，3以格式为YYYY-MM-DD输出
print(datetime.date.today().strftime("%d/%m/%Y"))#输出当天时间,格式为DD/MM/YYYY
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22) #很明显年推迟22年
print(day)
