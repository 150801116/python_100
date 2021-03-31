#题目 有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#注意审题呀是每个月都生，不是每三个月生，所以要有一个纪录，记下兔子年纪
print("请输入第几个月份：",end="")
n = int(input())
n1=1  #定义了三个int型 用于记录不同月份的兔子对数，单位是对,x表示成年兔
n2=0
n3=0
x=0
for i in range(1,n+1):
    x += n3
    temp_n1 = n1
    n1 = x
    temp_n2 = n2
    n2 = temp_n1
    n3 = temp_n2
    sum =x+n1+n2+n3
    print("第",i,"月的兔子总数是：",sum,"对")
    print("其中1月兔子：",n1)
    print("其中2月兔子：",n2)
    print("其中3月兔子：",n3)
    print("其中成年兔子：",x)

#答案解析版本
month=int(input('繁殖几个月？：'))
month_1=1
month_2=0
month_3=0
month_elder=0
for i in range(month):
    month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
    print('第%d个月共'%(i+1),month_1+month_2+month_3+month_elder,'对兔子')
    print('其中1月兔：',month_1)
    print('其中2月兔：',month_2)
    print('其中3月兔：',month_3)
    print('其中成年兔：',month_elder)
