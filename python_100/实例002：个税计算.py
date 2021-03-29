#题目 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？
#方法一从小到大
profit = int(input())  #input键盘输入进去的数据类型是str可以使用print(type(profit))查看数据类型
reward = 0
if profit <= 100000:
    reward = profit*0.1;
elif (profit > 100000)and(profit <= 200000):
    reward = (profit-100000) * 0.075+100000*0.1;
elif (profit > 200000)and(profit <= 400000):
    reward = (profit - 200000) * 0.05 +100000*0.075+ 100000 * 0.1;
elif (profit > 400000)and(profit <= 600000):
    reward = (profit - 400000) * 0.03+200000*0.05 +100000*0.075+ 100000 * 0.1;
elif (profit > 600000) and (profit <= 1000000):
    reward = (profit - 600000) * 0.015 + 200000*0.03+200000* 0.05 + 100000 * 0.075 + 100000 * 0.1;
elif (profit > 1000000):
    reward = (profit - 1000000) * 0.01+400000*0.015 + 200000*0.03+200000 * 0.05 + 100000 * 0.075 + 100000 * 0.1;
print("第一张方案：")
print(reward)

#方法二分区间计算
reward2 = 0
thresholds = [100000,100000,200000,200000,400000]  #阈值分段
rates = [0.1,0.075,0.05,0.03,0.015,0.01]   #对应阈值的奖金比例
for i in range(len(thresholds)):   #按thresholds和rates两个里面长度短的
    if profit <= thresholds[i]:
        reward2 += profit*rates[i]
        profit2 = 0
        break
    else:
        reward2 +=thresholds[i]*rates[i]
        profit -=thresholds[i]
reward2 +=profit*rates[-1] #大于100万的，前面循环次数只会计算100万以内的，超过100万的并未计算
print("第二种方案")
print(reward2)

