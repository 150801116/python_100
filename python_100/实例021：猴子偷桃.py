#题目 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
#解析，第10天想吃的时候，只剩一个，说明第9天吃完剩1个，则从第9天往前推，第8天为（1+1）*2=4，第7天是（4+1)*2=10...
t = 1
for i in range(9):
    num = (t+1)*2
    t = num
print("第一天一共摘了",num)

