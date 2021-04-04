#题目 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
#假设第五只猴子拿走的桃子个数是x,则那之前是5x+1,
for i in range(1,1000):  #i表示第5只猴子拿的桃子数目
    sum5 = 5*i+1
    if sum5%4!=0:
        continue
    else:
        sum4 = sum5*5/4+1
        if sum4%4!=0:
            continue
        else:
            sum3 = sum4*5/4+1
            if sum3%4!=0:
                continue
            else:
                sum2 = sum3*5/4+1
                if sum2%4!=0:
                    continue
                else:
                    sum1 =sum2*5/4+1
                    print("最初有",sum1,"个桃子")
                    break

#参考答案
if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while (i < 5) :
        x = 4 * j
        for i in range(0,5) :
            if(x%4 != 0) :
                break
            else :
                i += 1
            x = (x/4) * 5 +1
        j += 1
    print(x)


    for p in range(5):
        x=(x-1)/5*4
    print(x)