#题目 暂停一秒输出。
#这道题一拿到的时候，毫无思路，看到答案恍然大悟，time模块的sleep函数真香，且我真的用的不多
import time
print(time.time())  #返回当前时间的时间戳（1970纪元后经过的浮点秒数）
print(int(time.time())) #进行强制转换，变成int型，直接截取小数点后面的数字
print(str(int(time.time()))) #再一次强制转换chengstr型，为了后续使用切片截图最后两位数字
print(str(int(time.time()))[-2:]) #切片输出末尾两位
print("******")
for i in range(4):   #四个数字是1S内瞬时输出的，后面的一个for调用了sleep则会出现连续输出
    print(str(int(time.time()))[-2:])
print("*******")
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)