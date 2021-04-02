#题目 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def reverseShow(str):
    if len(str)!=1:     #把长度不为1 的条件放前面，因为我尝试过把print放前面，发现那种情况就输出一个，会有影响！
        reverseShow(str[1:])  #不能加return,因为有了return则后续的代码不执行！！！
    print(str[0],end="")
print("请输入5个字符：",end="")
str = input()
reverseShow(str)
