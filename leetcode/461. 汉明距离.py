'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.
示例:
输入: x = 1, y = 4
输出: 2
解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
'''
# x = 0
# l = bin(x)  #10进制转2进制的函数
# print(type(l))    #输出为0b1010 每一位都是str型并非Int型
#print(type(l))   #输出类似为str
#print(len(l)) #字符串也有长度的
# y = 1
# l1 = bin(y)
# a = list(l[2:])  #切割掉0b保留后面的，并用list保存
# print(a)
# print(len(a))
# b = list(l1[2:])
# print(b)
# print(len(b))
#print(type(a[0]))  #输出类似为str

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''#详细版本
        #首先先把x,y转成二进制用内置函数的方法：
        a = bin(x)
        b = bin(y)
        #再把前面的0b切割出去，生成list形式
        a_1 = list(a[2:])
        b_1 = list(b[2:])
        #比较长度，方便比较,且将短的补到跟长的一样长
        len_a = len(a_1)
        len_b = len(b_1)
        if len_a<len_b:
            l = len_b
            t = len_b-len_a
            for i in range(t):
                a_1.insert(0,'0')
        else:
            l = len_a
            t = len_a - len_b
            for i in range(t):
                b_1.insert(0,'0')
        num = 0
        # if (x == 0)or(y==0):
        #     return t
        for i in range(-1,-1-l,-1):
            if a_1[i]!=b_1[i]:
                num +=1
        return num
        '''
        #简化一下
        '''
        if (x==0)or(y==0):  #首先把存在某一个为0 的情况返回
            t = bin(x+y)
            #print(t)
            t = list(t[2:])
            #print(t)
            num = 0
            for i in range(len(t)):
                if t[i]=='1':
                    num  +=1
            return num

        a = bin(x)
        a = list(a[2:])
        b = bin(y)
        b = list(b[2:])
        if len(a)<len(b):
            for i in range(len(b)-len(a)):
                a.insert(0,'0')
        elif len(a)>len(b):
            for i in range(len(a)-len(b)):
                b.insert(0,'0')
        num = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                num +=1
        return num
        '''
        #大神版本巧用函数
        #x^y返回的是int型，先用bin()转换成二进制，再数里面的1个数即可
        return bin(x^y).count('1')  #大哥的脑瓜子咋这么厉害！值得注意的是里面的1是str型而不是int型





if __name__ == "__main__":
        #print("输入:",end="")
        #print("x=", end="")
        x = int(input())
        #print("y=", end="")
        y = int(input())
        num = Solution().hammingDistance(x,y)  #固定用法！(类名().方法名(形参))类外调用不需要写self
        print(num)

