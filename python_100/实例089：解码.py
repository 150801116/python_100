#题目 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
print("请输入需要加密的四位数：",end="")
n = input()
#print(type(n[2]))
x1 = (int(n[0]) + 5)%10
x2 = (int(n[1]) + 5)%10
x3 = (int(n[2]) + 5)%10
x4 = (int(n[3]) + 5)%10
x1,x4=x4,x1
x2,x3=x3,x2
print("加密后的四位数：",end="")
t = x1*1000+x2*100+x3*10+x4
print(t)
