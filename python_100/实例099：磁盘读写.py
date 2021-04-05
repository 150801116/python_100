#题目 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
if __name__=="__main__":
    fp = open('test.txt','r')
    a = fp.read()
    fp.close()

    fp = open('test1.txt','r')
    b = fp.read()
    fp.close()

    fp = open('test2.txt','w')
    l = list(a+b)
    # print(l)
    # print(type(l))
    l.sort()
    s = ''
    s = s.join(l)
    # print(s)
    # print(type(s))
    fp.write(s)
    fp.close()

