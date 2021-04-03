#题目 按逗号分隔列表。
#说实话我都没看懂这个题让我干嘛，那我们就看一下参考答案吧
#join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
#参考答案
L = [1,2,3,4,5]
print(','.join(str(n) for n in L))
#join()函数的使用
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))  #r-u-n-o-o-b
print (s2.join( seq ))  #runoob