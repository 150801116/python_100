#题目 时间函数举例3。
#Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代。
if __name__ == '__main__':
    import time
    #start = time.clock() #以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
    start = time.perf_counter()
    for i in range(3000):
        print(i)
    #end = time.clock()
    end = time.perf_counter()
    print('different is %6.3f' % (end - start))