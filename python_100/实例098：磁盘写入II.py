#题目 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
if __name__=="__main__":
    fp = open('test1.txt','w')
    print("请输入一个字符串")
    s = input()
    s = s.upper()  #将字符串中的小写字母转变成大写
    fp.write(s)
    fp.close()
    fp = open('test.txt','r')
    print(fp.read())
    fp.close()