#题目 两个变量值用函数互换。
def exchage(a,b):
    return (b,a)

if __name__ =="__main__":
    x,y=1,2
    print("交换前：x=%d,y=%d"%(x,y))
    (x,y)=exchage(x,y)
    print("交换后：x=%d,y=%d" %(x,y))