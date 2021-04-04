#题目 求0—7所能组成的奇数个数。
#分类讨论，最多是1位数，最多是8位数，最终求和
import math
sum = 4
for i in range(2,9): #
    sum +=7*4*math.pow(8,i-2)
print(sum)

#参考答案
print("------")
if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print(sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print('sum = %d' % sum)
