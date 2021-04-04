#题目 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
for i in range(7):
    print("请输入（1-50）的整数：",end="")
    n = int(input())
    print('*'*n)