#题目 学习使用auto定义变量的用法。
num = 2
def autofunc():
    num = 1
    print("内部num =",num)
    num +=1
for i in range(3):
    print("num = ",num)
    num +=1
    autofunc()
#预测输出：
# num = 2
# 内部num =1
#num = 3
# 内部num =1
#num = 4
# 内部num =1