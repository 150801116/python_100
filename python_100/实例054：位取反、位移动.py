#题目 取一个整数a从右端开始的4～7位。毫无思路，投降！
#程序分析 可以这样考虑：
#(1)先使a右移4位。
#(2)设置一个低4位全为1,其余全为0的数。可用(0<<4)
#(3)将上面二者进行&运算。

#参考答案
a=int(input('输入一个数字: '))
b=0                 #     0
b=~b                #     1
b=b<<4              # 10000
b=~b                #  1111
c=a>>4
d=c&b
print('a:',bin(a))
print('b:',bin(b))
print('c:',bin(c))
print('d:',bin(d))

print("---------------")
#还是没懂嘛。。。
a = int(input('input a number:\n'))
b1 = a >> 4
c = ~(~0 << 4)
d = b1 & c
print ('%o\t%o' %(a,d))