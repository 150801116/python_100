#题目 模仿静态变量(static)另一案例。
class Num:
    num = 1
    def inc(self):
        self.num +=1
        print("类里面的num = ",self.num)
if __name__=="__main__":
    num = 2
    inst = Num()  #初始化一个Num类
    for i in range(3):
        num +=1
        print("num = ",num)
        inst.inc()
#预测输出：
#num = 3
#类里面的num = 2
#num = 4
#类里面的num = 3
#num = 5
#类里面的num = 4