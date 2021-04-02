#题目 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
molecule = 2 #分子
denominator = 1 #分母
sum = 0 #总和
for i in range(20):
    sum += molecule/denominator
    molecule,denominator = (molecule+denominator),molecule
print("前20项和：",sum)