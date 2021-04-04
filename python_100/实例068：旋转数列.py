#题目 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
def houyi(n,m):
    l=len(n)
    n1=n[-m:]  #先保存好后续的m位
    #print(n1)
    for i in range(l-1,m-1,-1):
        n[i]=n[i-m]
    #print(n)
    for i in range(m):
        n[i]=n1[i]
list =[1,2,3,4,5,6,7,8,9,10]
houyi(list,2)
print(list)