#题目 暂停一秒输出，并格式化当前时间。
#在前一题的基础上，进行修正，很明显，那些函数我又不记得了！不对是我压根不知道！
#time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数 format 决定,人为理解为控制输出格式！！！非常关键
#Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准
import time
print(time.localtime())  #测试发现，如果输出当前时间的话，则参数可加可不加
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))  #%Y-%m-%d %H:%M:%S,这个输出格式已经被写死了，我尝试过换大小写，发现输出不对！
print("*******")
for i in range(4):
   print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
   time.sleep(1)