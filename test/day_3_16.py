#翻转字符串
'''
def reverseWords(input):
    inputWords = input.split(" ")
    print("inputWords")
    print(inputWords)
    inputWords = inputWords[-1::-1]
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    output = " ".join(inputWords)
    # 重新组合字符串
    return output
if __name__ =="__main__":
    input = "I like runoob"
    rw = reverseWords(input)
    print(rw)
'''
#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等
#整数范围是-5 到256共用一个内存地址

'''
x = True
y = False
z = False
print(x or y)
print(x or y and z)

if x or y and z:
    print("yes")
else:
    print("no")
#Python字符串格式化
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
#python3.6后出现f-string
#f-string 格式化字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去
#则不用判断%后面是什么了
name = "Runoob"
print(f'Hello {name}')
'''
'''
a,b=0,1
while b < 10:
    print(b)
    a,b=b,a+b #等价于n=b,m=a+b,a=n,b=m,先统一计算右边再赋值
'''
#猜数字
# number = 6
# guess = -1
# while(guess != number):
#     guess = int(input("请输入数字："))
#     if(guess == number):
#         print("恭喜你，你猜对了！")
#     elif(guess < number ):
#         print("猜的数字过小了！")
#     elif(guess > number):
#         print("猜的数字过大了！")

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)