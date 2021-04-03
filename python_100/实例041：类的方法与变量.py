#题目 模仿静态变量的用法。
#很久没遇到类了，有点手生，直接看参考答案吧
#参考答案
def dummy():
    i = 0
    print(i)
    i +=1
class cls:
    i = 0
    def dummy(self):
        print(self.i)
        self.i +=1
a = cls()
for i in range(50):
    dummy()   #输出一直为0 i=0,且i的生命周期只在函数内
    a.dummy() #i随着循环增加，i是作为类的属性保存的。