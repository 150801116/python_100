#题目 时间函数举例1
import time
if __name__=="__main__":
    print(time.ctime(time.time())) #把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
    print(time.asctime(time.localtime(time.time()))) #作用是格式化时间戳为本地的时间
    print(time.asctime(time.gmtime(time.time()))) #一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数
